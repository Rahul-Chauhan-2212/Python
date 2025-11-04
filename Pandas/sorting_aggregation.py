import pandas as pd

data = {
    "name" :["Rahul","Arun", "Xavier", "Vijay"],
    "age": [30, 20, 25, 25],
    "salary": [20000, 40000, 30000, 15000]
}

df = pd.DataFrame(data)

# Sorting
df.sort_values(by="name", ascending=True, inplace=True)
print(df)
df.sort_values(by="age", ascending=False, inplace=True)
print(df)
df.sort_values(by=["name","age"], ascending=[True,True], inplace=True)
print(df)

# Aggregation
print(df["age"].mean())

#Grouping
group = df.groupby("age")["salary"].sum()
print(group)

print(df.groupby(["age", "name"])["salary"].sum())

