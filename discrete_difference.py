import numpy as np
A = np.array([1,2,4,7,0])
n=int(input("n-value: "))
diff = np.diff(A,n)
print(f"Order {n} Difference:",diff)
