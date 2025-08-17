import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)

a = np.array_split(arr, 2)
# np.array_split(arr, 2)
# print(a)
# ar = np.arange(10,22,2).reshape(2,3)
# print(ar)

#3 dimensional array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(arr_3d)

for i in range(5,-2, -1):
    print(i)