import pandas as pd
import numpy as np

df = [20,0,12,-20,40, np.NaN, np.NaN]

print(df.isnull().sum())