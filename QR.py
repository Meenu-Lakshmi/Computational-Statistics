import numpy as np
A = np.array([[1,2],[3,4],[5,6]])
Q,R = np.linalg.qr(A)
print("Q:",Q)
print("R:",R)
