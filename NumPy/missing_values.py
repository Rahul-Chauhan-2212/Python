import numpy as np

array = np.array([1, 2, np.nan, np.nan, 5, np.nan, 7])
print(np.isnan(array))

# Complete missing number
cleaned_array = np.nan_to_num(array, nan=0)
print(cleaned_array)

cleaned_array = np.nan_to_num(array, nan=100)
print(cleaned_array)

array = np.array([1, 2, np.inf, np.inf, 5, -np.inf, 7])
print(np.isinf(array))

cleaned_array = np.nan_to_num(array, posinf=100, neginf=10)
print(cleaned_array)

