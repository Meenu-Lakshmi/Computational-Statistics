import numpy as np

array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[0, 5], [6, 7]])

kronecker_product = np.kron(array_a, array_b)

print("Kronecker Product:")
print(kronecker_product)
