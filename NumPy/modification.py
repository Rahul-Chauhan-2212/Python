import numpy as np

array = np.array([1, 2, 4, 5, 6])
# Insert in 1-D
array_2 = np.insert(array, 2, 3, 0)
print(array)
print(array_2)

# Insert in 2-D
array = np.array([[1, 2], [3, 4]])
array_2 = np.insert(array, 1, [5, 6], 0)
print(array)
print(array_2)

# Append add the end
array = np.array([1, 2, 3, 4, 5, 6])
array_2 = np.append(array, 7)
print(array_2)

# Concatenate
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
array_3 = np.concatenate((array_1, array_2), 0)
print(array_3)

# Remove
array = np.array([1, 2, 3, 4, 5, 6])
array_2 = np.delete(array, 3, 0)
print(array_2)

# Stacking
array = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
print(np.vstack(array))
print(np.hstack(array_2))

# Splitting
array = np.array([[1,2,3,4],
              [5,6,7,8]])
print(np.hsplit(array, 1))
print(np.vsplit(array, 2))