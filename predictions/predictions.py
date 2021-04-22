from keras.layers import Activation, Dense, Dropout, LSTM
from keras.models import Sequential,load_model
from .models import ModellingData
import numpy as np
from .data_prep import *
import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings("ignore")

def make_predictions(mobility_level,restriction_levels,vaccination_speed,table_name,rapid=False):
    # fetching data from database
    data = pd.DataFrame(ModellingData.objects.values())

    # saving date of the last part, as it will be lost at one point to rebuild it
    date = data["date_x"][90:150]

    # filling columns
    data = fill_mobility_columns(data,mobility_level,rapid)
    data = fill_restrictions_column(data,restriction_levels,rapid)
    data = fill_vaccination_speed(data,vaccination_speed)

    print(data[["mobility_transit","people_fully_vaccinated_per_hundred","c1_school_closing"]][80:110])
    print(data[["mobility_transit","people_fully_vaccinated_per_hundred","c1_school_closing"]].iloc[-1,:])

    # preparing data for model
    data = general_data_prep(data)
    data["british_strain"][90:150] = 1



    # loading model
    cases_model = load_model('covid_model.keras')

    # columns to trop
    cols_not = ["total_deaths_per_million","new_deaths_per_million","hosp_patients_per_million",
            'new_tests_per_thousand', 'positive_rate','tests_per_case',"reproduction_rate","total_cases_per_million"]
    
    # dropping columns, casting data to numpy
    cases_data = data.drop(cols_not,axis=1)
    cases_data = cases_data.to_numpy()

    # making 60 one forward predictions in a loop
    for i in range(60):
        pred_data = cases_data[i:90+i,:]
        value = cases_model.predict(pred_data.reshape(1,90,25))
        cases_data[90+i,0] = value

    # opening scaler to make inverse transformations
    with open('scaler.pkl', 'rb') as file:
        scaler = load(file)
    reverse_scaler = MinMaxScaler()
    reverse_scaler.min_,reverse_scaler.scale_ = scaler.min_[2], scaler.scale_[2]
    cases_predictions = pd.Series(reverse_scaler.inverse_transform(cases_data[90:,0].reshape(-1,1)).reshape(1,-1)[0])


    hosp_model = load_model("hosp_model.keras")

    cols_not = ["total_deaths_per_million","new_deaths_per_million",'new_tests_per_thousand', 'positive_rate','tests_per_case',
    "reproduction_rate","total_cases_per_million","british_strain"]

    hosp_data = data.drop(cols_not,axis=1).to_numpy()

    for i in range(60):
        pred_data = hosp_data[i:90+i,:]
        value = hosp_model.predict(pred_data.reshape(1,90,25))
        hosp_data[90+i,1] = value
    reverse_scaler = MinMaxScaler()
    reverse_scaler.min_,reverse_scaler.scale_ = scaler.min_[5], scaler.scale_[5]
    hosp_predictions = pd.Series(reverse_scaler.inverse_transform(hosp_data[90:,1].reshape(-1,1)).reshape(1,-1)[0])
    
    predictions = pd.DataFrame({"new_cases":cases_predictions,"hospitalizations":hosp_predictions,"date":date.to_list()})

    engine = create_engine('postgresql+psycopg2://postgres:figa997@localhost:5432/covid_19_in_poland')
    predictions.to_sql(table_name,con=engine,if_exists="replace")

def run_predictions():
        """
        Running different prediction scenarios. There are 4 different scenarios to choose from :

        1. Lifting all restrictions, mobility rapidly back to base levels, vaccination programme almost stalls 
        2. Lifting restrictions twice, one level down,every ten days, mobility slowly comes back to -10% of base, vaccinations continue as planned
        3. Lifting restrictions once, one level down, mobility slowly comes back to -10% of base, vaccinations continue as planned
        4. Keeping current restrictions, mobliity level stays -30% off base, vaccinations continue as planned 
        5. Current restrictions go one level up if possible, mobility levels -50%, vaccinations continue as planned

        """
        # 1
        make_predictions(0,0,10,"scenario 1",rapid=True)
        # 2
        make_predictions(-10,-2,30,"scenario 2",rapid=False)
        #3 
        make_predictions(-20,-1,30,"scenario 3",rapid=False)
        # 3 
        make_predictions(-30,0,30,"scenario 4",rapid=False)
        # 4 
        make_predictions(-50,1,30,"scenario 5",rapid=False)

        print("All done")
