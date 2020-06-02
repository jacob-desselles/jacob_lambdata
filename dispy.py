import pandas as pd
import numpy as np

df = [20,0,12,-20,40, 'NaN', 'NaN']
null = np.NaN
def isitnan(df):
    for x in df:
        if x == 'NaN':
            print('FALSE')
        else:
            print(x)
isitnan(df)

def splitdate(df):
    for x in df:
        df['day'] = df.index.day
        df['month'] = df.index.month
        df['year'] = df.index.year