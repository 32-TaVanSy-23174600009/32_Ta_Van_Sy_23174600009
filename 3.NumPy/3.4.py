import numpy as np

#  1: 
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[5] = 1
print(" 1 - arr_zeros:", arr_zeros)

#  2: 
arr_h = np.arange(10, 25)
arr_h_reversed = arr_h[::-1]
print(" 2 - arr_h đảo ngược:", arr_h_reversed)

#  3: Tạo arr_1 từ arr_k với các phần tử khác 0.
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[arr_k != 0]
print(" 3 - arr_1:", arr_1)

#  4: 
arr_1 = np.append(arr_1, [10, 20])
print(" 4 - arr_1 sau khi thêm 10 và 20:", arr_1)

#  5: 
arr_1 = np.insert(arr_1, 5, 100)
print(" 5 - arr_1 sau khi thêm 100 vào vị trí 5:", arr_1)

#  6: 
arr_1 = np.delete(arr_1, [0, 1, 2])
print(" 6 - arr_1 sau khi xóa các phần tử tại vị trí 0, 1, 2:", arr_1)
