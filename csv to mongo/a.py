import numpy as np
import pandas as pd


df = pd.read_csv('product_detail.csv')
df['category']= df['category'].str.split(',').str[0]
print(df['category'].unique())