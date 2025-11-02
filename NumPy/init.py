import numpy as np

# Initialization
list = [1, 2, 3 , 4, 5]
array = np.array(list)
print(array)

# 3*3 Matrix
array_2 = np.array([[1, 2 , 3], [4, 5, 6], [7, 8, 9]])
print(array_2)

# N d array
array_3 = np.ndarray((3, 3))
print(array_3)

# Matrix with only zeroes
array_4 = np.zeros((2,3))
print(array_4)

# Matrix with only ones
array_5 = np.ones((3, 3))
print(array_5)

# Identity Matrix
array_6 = np.eye(3)
print(array_6)

# Array with given value
array_7 = np.full((2, 3), 5)
print(array_7)

# Create array with range
array_8 = np.arange(1, 10)
print(array_8)