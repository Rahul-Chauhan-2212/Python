import numpy as np
from numpy.matrixlib.defmatrix import matrix

prices = [10, 20, 30]
final_prices = []
for price in prices:
    final_price = price - price / 10
    final_prices.append(final_price)
print(final_prices)

# Broadcasting
# expands smaller arrays into larger arrays, faster than arrays
prices = np.array([10, 20, 30])
discount = 10
final_prices = prices - (prices * discount / 100)
print(final_prices)

print(prices * 2)
print(prices + 10)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
result = matrix + vector
print(result)

array_2 = np.array([1, 2])
# print(matrix + array_2) # Value Error due to diff shape of matrix
