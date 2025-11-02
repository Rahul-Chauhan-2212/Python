import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])

# Reshaping
array_reshape = np.reshape(array, (2, 3))
print(array_reshape)

# Flattening
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array.flatten())  # returns copy of array
print(array.ravel())  # returns view of array so if you modify the ravel array it will change existing array
