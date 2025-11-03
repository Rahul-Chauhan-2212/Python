import pandas as pd

data = {
    'name': ["Rahul", "Shyam", "Ram"],
    "age": [10, 20, 30],
    "city": ["Mumbai", "Delhi", "Bangalore"]
}

df = pd.DataFrame(data)

print(df)
# df.to_csv("resources/output/write.csv", index=False)

#df.to_excel("resources/output/write.xlsx", index=False)

df.to_json("resources/output/write.json", index=False)

