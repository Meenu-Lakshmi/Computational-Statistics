import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

inner_product_vectors = np.dot(vector_a, vector_b)
print("Inner Product (Vectors):", inner_product_vectors)

inner_product_matrices = np.dot(matrix_a, matrix_b)
print("Inner Product (Matrix Multiplication):")
print(inner_product_matrices)


outer_product = np.outer(vector_a, vector_b)
print("Outer Product:")
print(outer_product)


cross_product = np.cross(vector_a, vector_b)
print("Cross Product:")
print(cross_product)
