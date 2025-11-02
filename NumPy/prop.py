import numpy as np

# Shape of array/matrix
array = np.array([[1, 2, 3], [4, 5, 6]])
print(np.shape(array))

# Size of array/no of elements in array
print(np.size(array))

# No of rows
print(np.size(array, 0))

# No of columns
print(np.size(array, 1))

# No of dimensions
array_1 = np.array([1, 2, 3])
array_2 = np.array([[1, 2, 3], [4, 5, 6]])
array_3 = np.array([[[1, 2],[3, 4], [5, 6], [7, 8]]])
print(np.ndim(array_1))
print(np.ndim(array_2))
print(np.ndim(array_3))
print(np.shape(array_3))

# Data Type of elements
print(np.array([1, 2, 3]).dtype)
print(np.array([1, 2, 3.4]).dtype)
print(np.array([1, 2, "3"]).dtype)
print(np.array([1, 2, True]).dtype)

# Converting type of elements in array
print(np.astype(array_1, str))



