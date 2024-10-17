import numpy as np
import matplotlib.pyplot as plt

A = np.array([1, 2, 3, 4, 5])
B = np.array([1, 4, 9, 16, 25])

plt.plot(A, B)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph from NumPy Array')
plt.show()
