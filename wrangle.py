#Wrangle Logs
#Imports for functions
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from env import host, user, password 
import os
import datetime
from sklearn.model_selection import train_test_split
import sklearn.preprocessing


##################
##### AQUIRE #####
##################

# Connection function to access Codeup Database and retrieve zillow dataset from mysql
def get_connection(db, user=user, host=host, password=password):
    '''
    This function creates a connection to Codeup Database with 
    info from personal env file (env file has user login information).
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}' 

def acquire_logs():
    '''
    This function reads in the zillow data from the Codeup 
    Database connection made from get_connection
    and returns a pandas DataFrame with all columns.
    '''
    # Query used to access logs on myql from codeup database
    sql_query = '''
    SELECT date, time, name, program_id, cohort_id,  user_id, path, ip, start_date, end_date
    FROM logs
    JOIN cohorts on cohorts.id = logs.cohort_id;
                '''

    
    return pd.read_sql(sql_query, get_connection('curriculum_logs'))  


##################
#### PREPARE #####
##################

# Function to prepare dataset for exploration

def prepare_logs():
    '''
    This function will acquire the dataset from acquire_logs
    and prepare for exploration by:
    - reformatting date/time columns and merging them
    - resetting date/time as index
    - adding weekday and month columns
    - renaming columns
    '''
    # Grabs dataframe from mysql and assigns it to a variable
    df = acquire_logs()
    # Reformats date and time
    

