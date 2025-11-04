import pandas as pd

df = pd.read_csv("resources/sales_data_sample.csv", encoding="latin1")

print(df)

print(df["ORDERNUMBER"])  # Selecting single column

print(df[["ORDERNUMBER", "DEALSIZE"]])  # Selecting multiple columns

print(df[df["QUANTITYORDERED"] > 50])  # Filtering data based on a condition

print(df[(df["QUANTITYORDERED"] > 50) & (df["DEALSIZE"] == 'Small')])  # Filtering data based on multiple conditions
