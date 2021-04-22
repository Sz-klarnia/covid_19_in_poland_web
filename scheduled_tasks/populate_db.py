import pandas as pd
import numpy as np
import psycopg2
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from .scripts import *
from sqlalchemy import create_engine
import time

def populate_database():
    """
    Function retrieves data from google spreadsheets about COVID-19 in Poland, created by Michał Rogalski.
    It uses google API to access data directly from google spreadsheets
    """
    
    
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    
    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    
    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # establish connection with db
    engine = create_engine('postgresql+psycopg2://postgres:figa997@localhost:5432/covid_19_in_poland')
    
    # get spreadsheet - COVID-19 in Poland
    sheet = client.open("Kopia pliku COVID-19 w Polsce")
    time.sleep(1)
    # cases report
    df = get_cases_report(sheet)
    df.to_sql("cases",con=engine,if_exists="replace")
    
    # regional report
    df = get_regional_case_report(sheet)
    df.to_sql("reg_cases",con=engine,if_exists="replace")
    
    # testing report
    df = get_testing_report(sheet)
    df.to_sql("testing",con=engine,if_exists="replace")
    
    # regional testing reports
    data = get_regional_testing_reports(sheet)
    for key in data.keys():
        data[key].to_sql(key,con=engine,if_exists="replace")
    
    # regional cases reports
    data = get_regional_cases_reports(sheet)
    for key in data.keys():
        data[key].to_sql(key,con=engine,if_exists="replace")
        
    # hospital load report
    df = get_hospital_load_report(sheet)
    df.to_sql("hospitalizations",con=engine,if_exists="replace")
    
    # regional hospital load reports
    data = get_regional_hospitalization_data(sheet)
    for key in data.keys():
        data[key].to_sql("hosp_in"+key,con=engine,if_exists="replace")
    time.sleep(1)
    # get spreadsheet - vaccinations data
    sheet = client.open("Kopia COVID-19 w Polsce - Szczepienia")
    
    # get vaccinations report
    df = get_vaccination_report(sheet)
    df.to_sql("vaccinations",con=engine,if_exists="replace")
    print("database populated")


def prepare_model_data(data,rest,mobility):
    """
    Function used to get latest avaliable modelling data to the database. Function takes dataframes with data.
    """
    # filter only used columns from restrictions
    col_idxs = [0,5,6,8,10,12,14,16,18,20,26,28,29,32,34,36,47]
    rest = rest[rest.columns[col_idxs]]

    # prepare date and location columns from restrictions
    rest["Date"] = [pd.to_datetime(".".join([str(x)[0:4],str(x)[4:6],str(x)[6:]])) for x in rest["Date"]]
    rest = rest.rename({"CountryName":"location","Date":"date"},axis=1)

    data["location"] = "Poland"
    mobility["location"] = "Poland"
    # saving only data from the last 90 days
    data = data[-90:]
    rest = rest[-90:]
    mobility = mobility[-90:]

    # create common key column for in all dfs to merge
    rest["location_date"] = [rest["location"].iloc[i]+" "+str(rest["date"].iloc[i])[:-9] for i in range(len(rest))]
    data["location_date"] = [data["location"].iloc[i]+" "+str(data["date"].iloc[i]) for i in range(len(data))]
    mobility["location_date"] = [mobility["location"].iloc[i]+" "+mobility["date"].iloc[i] for i in range(len(mobility))]

    # merging

    data = data.merge(rest,how="left",on="location_date").merge(mobility,how="left",on="location_date")
    # filling empty values
    data = data.fillna(method="bfill")
    data = data.fillna(method="ffill")
    # dropping duplicated cols
    data.drop(["location_y","date_y","location_date","location_x","location","date"],axis=1,inplace=True)
    # adding informations about british covid variant  
    data.date_x = data.date_x.apply(lambda x: pd.to_datetime(x))  
    data["british_strain"] = 0
    strain_data = {
        1:pd.to_datetime("01.02.2021",dayfirst=True),
        2:pd.to_datetime("20.02.2021",dayfirst=True),
        3:pd.to_datetime("07.03.2021",dayfirst=True),
        4:pd.to_datetime("15.03.2021",dayfirst=True)}

    idx1 = data[data.date_x==strain_data[1]].index[0]
    idx2 = data[data.date_x==strain_data[2]].index[0]
    idx3 = data[data.date_x==strain_data[3]].index[0]
    idx4 = data[data.date_x==strain_data[4]].index[0]
    data["british_strain"][idx1:idx2] = 1
    data["british_strain"][idx2:idx3] = 2
    data["british_strain"][idx3:idx4] = 3
    data["british_strain"][idx4:] = 4



    # droping unneceseary cols
    data.drop(["new_deaths","new_deaths_smoothed",'new_cases_smoothed_per_million',"hosp_patients",
           "new_tests_smoothed","new_tests_smoothed_per_thousand","total_cases","new_cases","new_cases_smoothed",
          "new_tests","total_tests","total_vaccinations","people_vaccinated","people_fully_vaccinated","new_vaccinations",
          "new_vaccinations_smoothed","new_vaccinations_smoothed_per_million","total_tests_per_thousand","new_deaths_smoothed_per_million","tests_units","total_deaths"],axis=1,inplace=True)
    
    # cast date to datetime
    data["date_x"] = data["date_x"].apply(lambda x: pd.to_datetime(x))
    # create empty extension of the data 60 days ahead with date column filled
    data = data.append(pd.DataFrame(np.zeros((60,data.shape[1])),columns=data.columns),ignore_index=True)
    data["date_x"].iloc[90:150] = pd.Series(pd.date_range(data["date_x"].iloc[89],data["date_x"].iloc[89]+ pd.Timedelta(59,"D")))

    # write to database
    engine = create_engine('postgresql+psycopg2://postgres:figa997@localhost:5432/covid_19_in_poland')
    data.to_sql("modelling_data",con=engine,if_exists="replace")