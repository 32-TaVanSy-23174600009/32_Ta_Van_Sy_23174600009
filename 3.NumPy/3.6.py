import numpy as np

#  1: 
arr = np.full((3, 3), True)
print(" 1 - arr với các giá trị True:\n", arr)

#  2: 
arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_ID.reshape(3, 3)
print("\n 2 - arr_2D ban đầu:\n", arr_2D)

# Chuyển cột 1 sang cột 3 và ngược lại
arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]]
print("\n 2 - arr_2D sau khi đổi thứ tự cột 1 và cột 3:\n", arr_2D)

#  3: 
arr_2D[[0, 1], :] = arr_2D[[1, 0], :]
print("\n 3 - arr_2D sau khi đổi thứ tự dòng 1 và dòng 2:\n", arr_2D)

#  4: 
arr_2D = arr_2D[::-1]
print("\n 4 - arr_2D sau khi đảo ngược các dòng:\n", arr_2D)

#  5: 
arr_2D = arr_2D[:, ::-1]
print("\n 5 - arr_2D sau khi đảo ngược các cột:\n", arr_2D)

#  6: 
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("\n 6 - arr_2D_null có giá trị rỗng không?:", has_nan)

#  7: 
arr_2D_null = np.nan_to_num(arr_2D_null, nan=0)
print("\n 7 - arr_2D_null sau khi thay thế giá trị null bằng 0:\n", arr_2D_null)
