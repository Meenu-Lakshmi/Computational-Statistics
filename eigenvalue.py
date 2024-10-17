import numpy as np
A = np.array([[1,2],[0,3]])
eigenvalues,eigenvectors = np.linalg.eig(A)
print("Eigenvalues:",eigenvalues)
print("Eigenvectors:",eigenvectors)
