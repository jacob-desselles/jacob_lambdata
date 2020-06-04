import pandas as pd
import numpy as np

df = [20,0,12,-20,40, 'NaN', 'NaN']
null = np.NaN
def isitnan(df):
    #Will scan any dataset for NaNs and will replace with 'FALSE', but it will first have to convert
    #NaN values to strings.
    for x in df:
        if x == 'NaN':
            print('FALSE')
        else:
            print(x)
isitnan(df)

def splitdate(df):
    #Will split any timedate-format columns into three separate columns.
    for x in df:
     df['day'] = df['datetime_utc'].dt.day
     df['month'] = df['datetime_utc'].dt.month
     df['year'] = df['datetime_utc'].dt.year
