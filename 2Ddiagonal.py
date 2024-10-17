import numpy as np

array_3d = np.random.random((4, 5, 6))  

diagonals = []

for i in range(array_3d.shape[0]):
    slice_2d = array_3d[i]  
    slice_diagonals = [slice_2d.diagonal(offset=k) for k in range(-slice_2d.shape[1] + 1, slice_2d.shape[0])]
    diagonals.append(slice_diagonals)

diagonals = np.array(diagonals)
print(diagonals)
