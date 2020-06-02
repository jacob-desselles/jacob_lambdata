import pandas as pd
import numpy as np

df = [20,0,12,-20,40, np.nan, np.nan]
null = np.NaN
def isitnan(df):
    for x in df:
        if null:
            print('FALSE')
        else:
            print(x)
isitnan(df)