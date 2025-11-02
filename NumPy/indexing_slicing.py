import numpy as np

# Accessing element in array
array = np.array([10, 20, 30, 40, 50])
print(array[0])
print(array[1])
print(array[-1])
# print(array[10])  # Index error

# Slicing
print(array[1:3])
print(array[1:5:2])
print(array[:4])
print(array[::2])
print(array[::-1])

# Fancy Indexing selecting multiple elements at once
print(array[[0, 2, 3]])

# Boolean masking
print(array[array % 20 == 0])
print(array[array > 20])
