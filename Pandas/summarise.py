import pandas as pd

df = pd.read_csv("resources/sales_data_sample.csv", encoding="latin1")
print(df.head(10))  # first 10 rows
print(df.tail(5))  # last 10 rows

print(df.info())  # displaying info of data sets

print(df.describe())  # descriptive summary of all data  like count, mean, std, min, 25%, 50%, 75%, max

print(df.shape) # shape row * columns

print(df.columns) # column names



