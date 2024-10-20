import numpy as np

# 1. 
arr = np.arange(10)
print("Array ban đầu:", arr)               
print("Kiểu dữ liệu của arr:", arr.dtype) 
print("Kích thước của arr:", arr.shape)    

# 2. 
arr_even = arr[arr % 2 == 0]  #  phần tử chẵn
arr_odd = arr[arr % 2 != 0]   #  phần tử lẻ
print("Array chẵn:", arr_even)
print("Array lẻ:", arr_odd)

# 3. Cập nhật mảng: các phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 != 0, 100, arr)  # Thay phần tử lẻ bằng 100, phần tử chẵn giữ nguyên
print("Array cập nhật (phần tử lẻ thay bằng 100):", arr_update_1)

