from operator import index

import pandas as pd

data = {
    "name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "age": [28, 34, 22, 30, 29, 40, 25, 32],
    "salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "performance_score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

# Adding Columns

## Using assignment
df["bonus"] = df["salary"] / 10
print(df)

## using insert
df.insert(0, "employee_id", df["age"] % 13)
print(df)

# Updating values

df.loc[0, "salary"] = 55000
print(df)

df["salary"] = df["salary"] * 1.05
print(df)

# Removing columns/rows
df.drop(columns="performance_score", inplace=True)
print(df)


