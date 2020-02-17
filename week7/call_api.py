# call_api.py

import pandas as pd

def call_api(w_type,n_data_pts):
    df = pd.read_csv('https://api.thingspeak.com/channels/12397/fields/4.csv?results=20')
    return df
