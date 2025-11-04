import pandas as pd

data = {
    "name": ["Ram", None, "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "age": [28, 34, 22, 30, None, 40, 25, 32],
    "salary": [50000, 60000, 45000, 52000, 49000, None, 48000, 58000],
    "performance_score": [85, 90, 78, 92, 88, 95, 80, None]
}

df = pd.DataFrame(data)
print(df)

# finding missing data
print(df.isnull())

print(df.isnull().sum())

# Drop missing data row/columns
#df.dropna(axis=0, inplace=True)
#print(df)

# fill missing data
#df.fillna(axis=0, inplace=True, value=0)
df["name"].fillna(value="", inplace=True)
df["age"].fillna(value=df["age"].mean(), inplace=True)
df["salary"].fillna(value=df["salary"].min(), inplace=True)
df["performance_score"].fillna(value=df["performance_score"].median(), inplace=True)
print(df)


# Interpolation - fill missing values based on estimation, works on mathematical columns

data = {
    "time": [1, 2, 3, 4, 5],
    "value": [10, None, 30, None, 50]
}
df = pd.DataFrame(data)
print(df)

df["value"] = df["value"].interpolate(method="linear")
print(df)