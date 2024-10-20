import numpy as np


arr_a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 8])

# 1. 
arr_c = np.intersect1d(arr_a, arr_b)
print("Các phần tử xuất hiện ở cả a và b:", arr_c)

# 2. 
unique_a = np.setdiff1d(arr_a, arr_b)
print("Phần tử chỉ có ở a:", unique_a)
# 3
arr_e = np.array([2,6,1,9,10,3,27,8,6,25,16])
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]

print("Mảng mới (chỉ chứa các phần tử từ 5 đến 10):", arr_f)