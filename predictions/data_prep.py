import pandas as pd
from .models import ModellingData
from statsmodels.tsa.ar_model import AutoReg
from pickle import load
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def interpolate_column(column,rng,value):
    column[-rng:] = np.NaN
    column.iloc[-1] = value
    column = column.interpolate()
    return column

def fill_mobility_columns(df,level,rapid=False):
    """
    Function prepares mobility columns in the dataframe for one forward prediction,filling values ahead with chosen threshold

    Args:
    df - data frame with mobility columns empty in future dates
    level - level of change in mobility in the future from the baseline in Google mobility report for Poland
    """
    


    columns = ['mobility_recreation',
       'mobility_grocery', 'mobility_parks', 'mobility_transit',
       'mobility_work']
    if rapid == True:
        for col in columns:
            df[col][90:] = level
    else:
        for col in columns:
            df[col]= interpolate_column(df[col], 60, level)
    
    return df

def fill_restrictions_column(df,restriction_level,rapid=False):
    """
    Function prepares restriction columns in the dataframe for one forward prediction,filling values ahead with chosen threshold. For now, the function can
    only assume 4 basic values - no restrictions, mild restrictions, severe restrictions and full lockdown, represented as: 0, 0.33, 0.66, 1. In
    the future I'd like to include ability to tweak every restriction levels separately.
    
    Args:
    df - data frame with mobility columns empty in future dates
    level - level of restrictions 
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
            df[col][90:] = restriction_level
            continue
        if restriction_level == 0:
            df[col][90:] = df[col][89]
            continue
        
        target_val = df[col][89] + restriction_level

        # checking if target value is not larger than
        if target_val > value:
            target_val = value
        if target_val < 0:
            target_val = 0
        
        if restriction_level > 0:
            step_change = 1
        if restriction_level < 0:
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
        # step 3 - more steps than three currently not supported
        # adding value
        df[col][110:120] = df[col][109] + step_change
        # checking if target reached
        if df[col][119] == target_val:
            df[col][120:] = target_val
            continue


        
    return df

def fill_vaccination_speed(df,target):
    """
    Function prepares vaccination columns for prediction, filling the future values according to the chosen speed. Currently function only accepts
    three values of the speed parameter: slower (represented as 0.5), constant (represented as 1) and faster (1.5). Filling algorythm:
    predict by AutoReg model with lag set to 10, calculate difference between last value and today, multiply by speed.

    """
    cols = ['total_vaccinations_per_hundred',
       'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']
    target_vals = [1.33,1,0.66]
    for i in range(len(cols)):
        df[cols[i]] = interpolate_column(df[cols[i]], 60, target*target_vals[i])
        
    return df

def general_data_prep(df):
    """ data prep same for each model - removing partial indexes, scaling data that's constant for each country and
    differen between them"""
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
    
    df[mobility] = df[mobility].shift(21).fillna(method = "bfill")
    df[restrictions] = df[restrictions].shift(21).fillna(method = "bfill")
    df[vacc] = df[vacc].shift(21).fillna(method = "bfill")

    
    return df