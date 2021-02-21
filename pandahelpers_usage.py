import pandas as pd
from pandashelpers.helpers import one_hot_encode, label_encode, find_fill_na

df = pd.read_csv('Data.csv')

df = one_hot_encode(df, 'Country')

df = label_encode(df, 'Purchased')

df = find_fill_na(df, col=['Age', 'Salary'])

print(df.head())

