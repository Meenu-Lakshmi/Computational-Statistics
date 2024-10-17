import numpy as np
x = np.array([1,2,3,4])
y = np.array([4,5,6,7])
correlation_matrix = np.corrcoef(x,y)
print("Pearson Correlation Coefficient:", correlation_matrix)
