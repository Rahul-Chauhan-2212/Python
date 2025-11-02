import numpy as np

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
result = [x + y for x, y in zip(list_1, list_2)]
print(result)
# Vectorization
# Faster than loops, used in matrix
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
result = array_1 + array_2
print(result)

result = array_1 * array_2
print(result)