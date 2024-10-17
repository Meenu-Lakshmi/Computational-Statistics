import numpy as np

matrix = np.array([[1, 2], [3, 4]])

determinant = np.linalg.det(matrix)

if determinant != 0:
    matrix_inv = np.linalg.inv(matrix)
    print("Inverse of the matrix:")
    print(matrix_inv)
else:
    print("Matrix is singular and cannot be inverted.")
