import pandas as pd
from .models import ModellingData
from statsmodels.tsa.ar_model import AutoReg
from pickle import load
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def interpolate_column(column,start_idx,rng,value):
    column[start_idx:start_idx+rng] = np.NaN
    column.iloc[start_idx+rng] = value
    column = column.interpolate()
    return column

def fill_mobility_columns(df,col_changes):
    """
    Function prepares mobility columns in the dataframe for one forward prediction,filling values ahead with chosen threshold

    Args:
    df - data frame with mobility columns empty in future dates
    level - level of change in mobility in the future from the baseline in Google mobility report for Poland
    """

    for col,value in col_changes.items():
        df[col]= interpolate_column(df[col],90, 20, (df[col][69:90].mean())+value[0])
        df[col]= interpolate_column(df[col],110, 39, value[1])
    
    return df

def fill_restrictions_column(df,cols_vals,rapid=False):
    """
    Function prepares restriction columns in the dataframe for one forward prediction. Restriction levels are changed according to the changes supplied
    in cols_vals, one step every ten days untill reaching target
    
    Args:
    df - data frame with mobility columns empty in future dates
    cols_vals - dictionary with restriction values by column
    """

    # restriction codes with their maximum values
    cols =  {'c1_school_closing':3, 
    'c2_workplace_closing': 3, 
    'c3_cancel_public_events': 2,
    'c4_restrictions_on_gatherings': 4, 
    'c5_close_public_transport':2,
    'c6_stay_at_home_requirements':3,
    'c7_restrictions_on_internal_movement':2,
    'c8_international_travel_controls':4,
    'h1_public_information_campaigns':2,
    'h2_testing_policy':3, 
    'h3_contact_tracing':2, 
    'h6_facial_coverings':4,
    'h7_vaccination_policy':5, 
    'h8_protection_of_elderly_people':3}
    # rapid change - value changes in one step to target value
    for col,value in cols.items():
        if rapid == True:
            df[col][90:] = cols_vals
            continue
        if cols_vals[col] == 0:
            df[col][90:] = df[col][89]
            continue
        
        target_val = cols_vals[col]

        # checking if target value is not larger than maximum value for column
        if target_val > value:
            target_val = value

        # checking wether restrictions are tighter or looser to change values every step in the right direction
        if cols_vals[col] > df[col][89]:
            step_change = 1
        if cols_vals[col] < df[col][89]:
            step_change = -1
        
        if df[col][89] == target_val:
            df[col][90:] = target_val
            continue
        # step 1
        # adding value
        df[col][90:100] = df[col][89] + step_change
        # checking if target reached
        if df[col][99] == target_val:
            df[col][100:] = target_val
            continue
        # step 2
        # adding value
        df[col][100:110] = df[col][99] + step_change
        # checking if target reached
        if df[col][109] == target_val:
            df[col][110:] = target_val
            continue
        # step 3
        # adding value
        df[col][110:120] = df[col][109] + step_change
        # checking if target reached
        if df[col][119] == target_val:
            df[col][120:] = target_val
            continue
        # step 4
        # adding value
        df[col][120:130] = df[col][119] + step_change
        # checking if target reached
        if df[col][129] == target_val:
            df[col][130:] = target_val
            continue


        
    return df

def fill_vaccination_speed(df,target):
    """
    Function prepares vaccination columns for prediction, filling the future values according to the chosen target of vaccinated people at the end of
    the period using interpolation.

    Args:
    df - data frame of prediction data with vaccinations columns empty and ready to fill
    target - target of people vaccinated with at least one dose at the end of the period
    """
    cols = ['total_vaccinations_per_hundred',
       'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']
    
    # modifiers of target. 1.33 for doses given, 0.66 for fully vaccinated
    target_vals = [1.33,1,0.66]
    for i in range(len(cols)):
        df[cols[i]] = interpolate_column(df[cols[i]], 89, 60, target*target_vals[i])
        
    return df

def general_data_prep(df):
    """ Scaling, filling nan values, dropping unneceseary columns, shifting columns"""
    # dropping aggregate indexes
    df.drop(["stringency_index","containmenthealthindex","index"],axis=1,inplace=True)
    
    
    # dropping date - we know that data is ordered in the right way and datetime fields are not scalable
    df.drop("date_x",axis=1,inplace=True)

            
    # in some places values are negative, and they can't be. Filling these values with a 0. Location col is a string col
    # mobility cols naturally have values below zero
    for col in df.columns:
        if col not in ["location",'mobility_recreation',
       'mobility_grocery', 'mobility_parks', 'mobility_transit',
       'mobility_work', 'mobility_residential']:
            idx = df[df[col]<0].index
            if len(idx) > 0:
                df[col][idx] = np.NaN
    # interpolate nans imputed in previous step
    df = df.interpolate("linear")
    
    # saving columns to paste back after scaling
    cols = df.columns

    # scaling chosen columns
    with open('scaler.pkl', 'rb') as file:
        scaler = load(file)
    df = scaler.transform(df)
    # reconstructing dataframe
    df = pd.DataFrame(df,columns=cols)
    
    
    mobility = ['mobility_recreation', 'mobility_grocery', 'mobility_parks',
       'mobility_transit', 'mobility_work', 'mobility_residential']
    
    
    
    restrictions = ['c1_school_closing', 
    'c2_workplace_closing', 
    'c3_cancel_public_events',
    'c4_restrictions_on_gatherings', 
    'c5_close_public_transport',
    'c6_stay_at_home_requirements',
    'c7_restrictions_on_internal_movement',
    'c8_international_travel_controls',
    'h1_public_information_campaigns',
    'h2_testing_policy',
    'h3_contact_tracing', 
    'h6_facial_coverings',
    'h7_vaccination_policy', 
    'h8_protection_of_elderly_people']
    vacc = ['total_vaccinations_per_hundred',
       'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']
    
    # Columns representing restrictions, mobility and vaccination data are all shifted by three weeks, because all of these actions have delayed effects
    df[mobility] = df[mobility].shift(21).fillna(method = "bfill")
    df[restrictions] = df[restrictions].shift(21).fillna(method = "bfill")
    df[vacc] = df[vacc].shift(21).fillna(method = "bfill")

    
    return df