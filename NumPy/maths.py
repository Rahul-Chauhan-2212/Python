import numpy as np

array = np.array([1, 2, 3])
# Performs math operations on each element of numpy array
print(array+2)
print(array-1)
print(array*3)
print(array/2)
print(array%2)

# Aggregate function
print(np.sum(array))
print(np.average(array))
print(np.min(array))
print(np.max(array))

# Statistical Functions
print(np.mean(array))
print(np.std(array))
print(np.var(array))