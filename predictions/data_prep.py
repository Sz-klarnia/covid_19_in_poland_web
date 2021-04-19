import pandas as pd
from .models import ModellingData
from statsmodels.tsa.ar_model import AutoReg
from pickle import loads

def fill_mobility_columns(df,level):
    """
    Function prepares mobility columns in the dataframe for one forward prediction,filling values ahead with chosen threshold

    Args:
    df - data frame with mobility columns empty in future dates
    level - level of change in mobility in the future from the baseline in Google mobility report for Poland
    """
    columns = ['mobility_recreation',
       'mobility_grocery', 'mobility_parks', 'mobility_transit',
       'mobility_work']

    for col in columns:
        df["column"][90:150] = level
    
    return df

def fill_restrictions_column(df,restriction_levels):
    """
    Function prepares restriction columns in the dataframe for one forward prediction,filling values ahead with chosen threshold. For now, the function can
    only assume 4 basic values - no restrictions, mild restrictions, severe restrictions and full lockdown, represented as: 0, 0.33, 0.66, 1. In
    the future I'd like to include ability to tweak every restriction levels separately.
    
    Args:
    df - data frame with mobility columns empty in future dates
    level - level of restrictions 
    """

    # restriction codes with their maximum values
    cols =  {'C1_School closing':3 , 
    'C2_Workplace closing': 3, 
    'C3_Cancel public events': 2,
    'C4_Restrictions on gatherings': 4, 
    'C5_Close public transport':2,
    'C6_Stay at home requirements':3,
    'C7_Restrictions on internal movement':2,
    'C8_International travel controls':4,
    'H1_Public information campaigns':2,
    'H2_Testing policy':3, 
    'H3_Contact tracing':2, 
    'H6_Facial Coverings':4,
    'H7_Vaccination policy':5, 
    'H8_Protection of elderly people':3}

    for col,value in cols.items():
        df[col][90:150] = value*restriction_levels
    
    return df

def fill_vaccination_speed(df,speed):
    """
    Function prepares vaccination columns for prediction, filling the future values according to the chosen speed. Currently function only accepts
    three values of the speed parameter: slower (represented as 0.5), constant (represented as 1) and faster (1.5). Filling algorythm:
    predict by AutoReg model with lag set to 10, calculate difference between last value and today, multiply by speed.

    """
    cols = ['total_vaccinations_per_hundred',
       'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']

    for cols in col:
        autoregressor = AutoReg(data[col][0:90], lags=10).fit()
        data[col][90:150] = autoregressor.predict(start=90,end=149)
        diffs = [data[col][i]-data[col][i-1] for i in range(90:150)] * speed
        data[col[90:150]] = [data[col][i-1]+diffs[i] for i in range(90:150)]
        
    return df

def general_data_prep(df):
    """ data prep same for each model - removing partial indexes, scaling data that's constant for each country and
    differen between them"""
    socioecon = ['population_density', 'median_age', 'aged_65_older',
       'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers',
       'life_expectancy', 'human_development_index']
    df.drop(socioecon,axis=1,inplace=True)
    # dropping partial indexes
    df.drop(["stringency_index","ContainmentHealthIndex"],axis=1,inplace=True)
    
    
    # dropping date - we know that data is ordered in the right way and datetime fields are not scalable
    df.drop("date",axis=1,inplace=True)
    # all countries have a values in vaccinations fields before start of vaccination programme, these must be put to 0
    vacc = ['total_vaccinations_per_hundred',
       'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']
    for country in df.location.unique():
        start_country = df[df.location == country].index[0]
        start_vacc = df[(df.location==country)&(df.total_vaccinations_per_hundred < 3)].index[0]
        for col in vacc:
            df[col][start_country:start_vacc] = 0
            
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
    locs = df.location
    df.drop("location",axis=1,inplace=True)
    cols = df.columns

    # scaling chosen columns
    scaler = load(open('scaler.pkl', 'rb'))
    df = scaler.transform(df)
    # reconstructing dataframe
    df = pd.DataFrame(df,columns=cols)
    df["location"] = locs
    
    
    mobility = ['mobility_recreation', 'mobility_grocery', 'mobility_parks',
       'mobility_transit', 'mobility_work', 'mobility_residential']
    
    
    
    restrictions = ['C1_School closing', 'C2_Workplace closing', 'C3_Cancel public events',
       'C4_Restrictions on gatherings', 'C5_Close public transport',
       'C6_Stay at home requirements', 'C7_Restrictions on internal movement',
       'C8_International travel controls', 'H1_Public information campaigns',
       'H2_Testing policy', 'H3_Contact tracing', 'H6_Facial Coverings',
       'H7_Vaccination policy', 'H8_Protection of elderly people']
    
    for country in data_countries.keys():

        data_countries[country][mobility] = data_countries[country][mobility].shift(21).fillna(method = "bfill")
        data_countries[country][restrictions] = data_countries[country][restrictions].shift(21).fillna(method = "bfill")

    
    return data_countries