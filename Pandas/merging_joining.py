import pandas as pd

# merging two data frames

df_customer = pd.DataFrame({
    'customer_id': [101, 102, 103, 104],
    'name': ['Rahul', 'Ankit', 'Sagar', 'Priya'],
    'city': ['Pune', 'Delhi', 'Indore', 'Mumbai']
})

df_orders = pd.DataFrame({
    'order_id': [5001, 5002, 5003, 5004, 5005],
    'customer_id': [101, 103, 101, 104, 105],
    'amount': [1500, 2200, 800, 4500, 1250]
})

print(df_customer)
print(df_orders)

merged_inner = pd.merge(df_customer, df_orders, on="customer_id", how="inner")

print(merged_inner)

merged_outer = pd.merge(df_customer, df_orders, on="customer_id", how="outer")
print(merged_outer)

merged_left = pd.merge(df_customer, df_orders, on="customer_id", how="left")
print(merged_left)

merged_right = pd.merge(df_customer, df_orders, on="customer_id", how="right")
print(merged_right)

merged_cross = df_customer.merge(df_orders, how='cross')
print(merged_cross)
print(merged_cross.shape)

# Concatenate
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['A', 'B', 'C']
})

df_b = pd.DataFrame({
    'id': [4, 5],
    'name': ['D', 'E'],
    'city': ['Pune', 'Delhi']
})
df_combined = pd.concat([df_a, df_b], axis=0, ignore_index=True)
print(df_combined)

df_combined = pd.concat([df_a, df_b], axis=1, ignore_index=True)
print(df_combined)
