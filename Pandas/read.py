import pandas as pd

# read data from csv using pandas into dataframe
df = pd.read_csv("resources/sales_data_sample.csv", encoding="latin1")
print(df)

# read data from excel using pandas into dataframe
# pip install xlrd --- for xls
# pip install openpyxl -- for xlsx
df = pd.read_excel("resources/Sample - Superstore.xls", engine="xlrd")
print(df.head())


# read data from json using pandas into dataframe
df = pd.read_json("resources/sample_Data.json")
print(df)