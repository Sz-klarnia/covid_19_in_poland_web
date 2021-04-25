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
    """
    Functions fills the data according to specified arguments and makes one forward predictions for 60 days ahead.

    Args:
    mobility_level: list of length: 1 if making rapid changes, 2 if making continuous changes. List items specify levels of mobility change
    restrictions_levels: dictionary. Keys are column names, values specify how much the value of a column should change
    vaccination_speed: level of vaccination supposed to be reached in 60 days
    table_name: name of the table in the database that will store predictions.
    rapid: value of a flag used in filling mobility and restrictions columns
    """
    # fetching data from database
    data = pd.DataFrame(ModellingData.objects.values())

    # saving date of the last part, as it will be lost at one point to rebuild it
    date = data["date_x"][90:150]

    # filling columns
    data = fill_mobility_columns(data,mobility_level)
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
        data["new_cases_per_million"][90+i] = value

    # opening scaler to make inverse transformations
    with open('scaler.pkl', 'rb') as file:
        scaler = load(file)
    reverse_scaler = MinMaxScaler()
    reverse_scaler.min_,reverse_scaler.scale_ = scaler.min_[2], scaler.scale_[2]
    cases_predictions = pd.Series(reverse_scaler.inverse_transform(cases_data[90:,0].reshape(-1,1)).reshape(1,-1)[0])

    # Predicting number of hospitalized patients
    

    hosp_model = load_model("hosp_model.keras")

    cols_not = ["total_deaths_per_million","new_deaths_per_million",'new_tests_per_thousand', 'positive_rate','tests_per_case',
    "reproduction_rate","total_cases_per_million"]

    hosp_data = data.drop(cols_not,axis=1).to_numpy()

    for i in range(60):
        pred_data = hosp_data[i:90+i,:]
        value = hosp_model.predict(pred_data.reshape(1,90,26))
        hosp_data[90+i,1] = value
        data["hosp_patients_per_million"][90+i] = value
    reverse_scaler = MinMaxScaler()
    reverse_scaler.min_,reverse_scaler.scale_ = scaler.min_[5], scaler.scale_[5]
    hosp_predictions = pd.Series(reverse_scaler.inverse_transform(hosp_data[90:,1].reshape(-1,1)).reshape(1,-1)[0])

    # predicting number of new deaths

    deaths_model = load_model("deaths_model.keras")

    cols_not = ["total_deaths_per_million",
            'new_tests_per_thousand', 'positive_rate','tests_per_case',"reproduction_rate","total_cases_per_million"]

    deaths_data = data.drop(cols_not,axis=1).to_numpy()

    for i in range(60):
        pred_data = deaths_data[i:90+i,:]
        value = deaths_model.predict(pred_data.reshape(1,90,27))
        deaths_data[90+i,1] = value
    reverse_scaler = MinMaxScaler()
    reverse_scaler.min_,reverse_scaler.scale_ = scaler.min_[3], scaler.scale_[3]
    deaths_predictions = pd.Series(reverse_scaler.inverse_transform(deaths_data[90:,1].reshape(-1,1)).reshape(1,-1)[0])
    
    # constructing dataframe with predictions and dates
    predictions = pd.DataFrame({"new_cases_per_million":cases_predictions,"hosp_patients_per_million":hosp_predictions,"date":date.to_list(),"new_deaths_per_million":deaths_predictions})

    # saving data to database
    engine = create_engine('postgresql+psycopg2://postgres:figa997@localhost:5432/covid_19_in_poland')
    predictions.to_sql(table_name,con=engine,if_exists="replace")

def run_predictions():
        """
        Running different prediction scenarios. There are 4 different scenarios to choose from :

        1. Lifting all restrictions, mobility rapidly comes back to +20% from the base, vaccination programme almost stalls 
        2. Lifting restrictions twice, one level down,every ten days, mobility slowly comes back to 0% of base, vaccinations continue as planned
        3. Lifting restrictions once, one level down, mobility slowly comes back to -15% of base, vaccinations continue as planned
        4. Keeping current restrictions, mobliity level stays the same off base, vaccinations continue as planned 
        5. Current restrictions go one level up if possible, mobility levels drops back to -50%, vaccinations continue as planned

        """
        # Levels of restrictions for each scenario
        restrictions_dicts = [
            {"c1_school_closing":1,
            "c2_workplace_closing":1,
            "c3_cancel_public_events":1,
            "c4_restrictions_on_gatherings":1,
            "c5_close_public_transport":0,
            "c6_stay_at_home_requirements":0,
            "c7_restrictions_on_internal_movement":0,
            "c8_international_travel_controls":1,
            "h1_public_information_campaigns":2,
            "h2_testing_policy":2,
            "h3_contact_tracing":1,
            "h6_facial_coverings":1,
            "h7_vaccination_policy":3,
            "h8_protection_of_elderly_people":3},
            {"c1_school_closing":2,
            "c2_workplace_closing":2,
            "c3_cancel_public_events":2,
            "c4_restrictions_on_gatherings":2,
            "c5_close_public_transport":1,
            "c6_stay_at_home_requirements":0,
            "c7_restrictions_on_internal_movement":0,
            "c8_international_travel_controls":1,
            "h1_public_information_campaigns":2,
            "h2_testing_policy":2,
            "h3_contact_tracing":1,
            "h6_facial_coverings":1,
            "h7_vaccination_policy":3,
            "h8_protection_of_elderly_people":3},
            {"c1_school_closing":3,
            "c2_workplace_closing":3,
            "c3_cancel_public_events":2,
            "c4_restrictions_on_gatherings":4,
            "c5_close_public_transport":1,
            "c6_stay_at_home_requirements":1,
            "c7_restrictions_on_internal_movement":1,
            "c8_international_travel_controls":3,
            "h1_public_information_campaigns":2,
            "h2_testing_policy":2,
            "h3_contact_tracing":1,
            "h6_facial_coverings":2,
            "h7_vaccination_policy":3,
            "h8_protection_of_elderly_people":3},
            {"c1_school_closing":3,
            "c2_workplace_closing":3,
            "c3_cancel_public_events":2,
            "c4_restrictions_on_gatherings":4,
            "c5_close_public_transport":2,
            "c6_stay_at_home_requirements":3,
            "c7_restrictions_on_internal_movement":2,
            "c8_international_travel_controls":3,
            "h1_public_information_campaigns":1,
            "h2_testing_policy":2,
            "h3_contact_tracing":1,
            "h6_facial_coverings":4,
            "h7_vaccination_policy":3,
            "h8_protection_of_elderly_people":3}
        ]

# levels of mobility for each scenario
        mobility_dicts = [
            {'mobility_recreation':(50,0),
       'mobility_grocery':(0,0),
       'mobility_parks':(20,0),
        'mobility_transit':(40,0),
       'mobility_work':(20,0)},
       {'mobility_recreation':(35,0),
       'mobility_grocery':(0,0),
       'mobility_parks':(10,0),
        'mobility_transit':(30,0),
       'mobility_work':(10,0)},
       {'mobility_recreation':(30,0),
       'mobility_grocery':(0,0),
       'mobility_parks':(10,0),
        'mobility_transit':(25,0),
       'mobility_work':(5,-12)},
        {'mobility_recreation':(10,-17),
       'mobility_grocery':(0,0),
       'mobility_parks':(0,0),
        'mobility_transit':(0,-24),
       'mobility_work':(0,-17)},
       {'mobility_recreation':(-15,-32),
       'mobility_grocery':(0,0),
       'mobility_parks':(-15,-15),
        'mobility_transit':(-15,-35),
       'mobility_work':(-15,-30)}
        
        ]
        

        


        # 1
        make_predictions(mobility_dicts[0],0,10,"scenario 1",rapid=True)
        # 2
        make_predictions(mobility_dicts[1],restrictions_dicts[0],30,"scenario 2",rapid=False)
        #3 
        make_predictions(mobility_dicts[2],restrictions_dicts[1],30,"scenario 3",rapid=False)
        # 3 
        make_predictions(mobility_dicts[3],restrictions_dicts[2],30,"scenario 4",rapid=False)
        # 4 
        make_predictions(mobility_dicts[4],restrictions_dicts[3],30,"scenario 5",rapid=False)

        print("All done")
