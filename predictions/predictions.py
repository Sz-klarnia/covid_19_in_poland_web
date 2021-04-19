from keras.layers import Activation, Dense, Dropout, LSTM
from keras.models import Sequential,load_model
from .models import ModellingData
from .data_prep import *
import pandas as pd
from sqlalchemy import create_engine

def make_predictions(mobility_level,restriction_levels,vaccination_speed,table_name):
    data = ModellingData.objects.values()

    data = fill_mobility_columns(data,mobility_level)
    data = fill_restrictions_column(data,restriction_levels),
    data = fill_vaccination_speed(data,vaccination_speed)

    data = general_data_prep(data)

    cases_model = load_model('covid_model.keras')

    cols_not = ["total_deaths_per_million","new_deaths_per_million","icu_patients_per_million","hosp_patients_per_million",
            'new_tests_per_thousand', 'positive_rate','tests_per_case','weekly_icu_admissions_per_million','weekly_hosp_admissions_per_million',"reproduction_rate","total_cases_per_million"]

    cases_data = data.drop(cols_not,axis=1)

    for i in range(60):
        pred_data = cases_data[i:90+i,:]
        value = cases_model.predict(pred_data.reshape(1,90,24))
        cases_data[90+i,0] = value

    cases_predictions = cases_data[90:,0]

    hosp_model = load_model("hosp_model.keras")

    cols_not = ["total_deaths_per_million","new_deaths_per_million","icu_patients_per_million",
            'new_tests_per_thousand', 'positive_rate','tests_per_case','weekly_icu_admissions_per_million','weekly_hosp_admissions_per_million',"reproduction_rate","total_cases_per_million"]

    hosp_data = data.drop(cols_not,axis=1)

    for i in range(60):
        pred_data = hosp_data[i:90+i,:]
        value = hosp_model.predict(pred_data.reshape(1,90,25))
        hosp_data[90+i,1] = value
    hosp_predictions = hosp_data[90:,1]

    predictions = pd.DataFrame({"new_cases":cases_predictions,"hospitalizations":hosp_predictions})

    engine = create_engine('postgresql+psycopg2://postgres:figa997@localhost:5432/covid_19_in_poland')
    data.to_sql(table_name,con=engine,if_exists="replace")

    def run_predictions():
        """
        Running different prediction scenarios. Currently, there are 12 different scenarions defined user will be able :

        1. Lifting all restrictions, mobility comes back to base levels, vaccination programme continues  
        2. Lifting all restrictions, mobility stays decreased by 20%, vaccination programme continues
        3. Small restrictions, mobility decreased by 20%, vaccinations continue
        4. Small restrictions, mobility decreased by 30%, vaccinations continue
        5. Severe restrictions, mobility decreased by 30%, vaccinations continue
        6. Severe restrictions, mobility decreased by 50%, vaccinations contiune
        7. Full lockdown, mobility decreased by 50%, vaccinations continue
        8. Full lockdown, mobility decreased by 60%, vaccinations continue
        9. Severe restrictions, mobility decreased by 30%, vaccinations speed up
        10. Severe restrictions, mobility decreased by 30%, vaccinations slow down
        11. Full lockdown, mobility decreased by 60%, vaccinations speed up
        12. Lifting all restrictions, mobility comes back to base levels, vaccination slow down
        """
        print("running_predicions")
        # 1
        make_predictions(0,0,1,"scenario 1")
        # 2
        make_predictions(0,-0.2,1,"scenario 2")
        # 3 
        make_predictions(0.33,-0.2,1,"scenario 3")
        # 4 
        make_predictions(0.33,-0.3,1,"scenario 4")
        # 5
        make_predictions(0.66,-0.3,1,"scenario 5")
        # 6 
        make_predictions(0.66,-0.5,1,"scenario 6")
        # 7 
        make_predictions(1,-0.5,1,"scenario 7")
        # 8 
        make_predictions(1,-0.6,1,"scenario 8")
        # 9 
        make_predictions(0.66,-0.3,1.5,"scenario 9")
        # 10
        make_predictions(0.66,-0.3,0.5,"scenario 10")
        # 11
        make_predictions(1,-0.6,1.5,"scenario 11")
        # 12 
        make_predictions(0,0,0.5,"scenario 12")