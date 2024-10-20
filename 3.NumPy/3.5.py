import numpy as np


with open('C:/laptrinhaaa/python học trên lớp/Python Kỳ 3/Btap/3.NumPy/heights_1.txt', 'r') as file:
    height = [float(line.strip()) for line in file if line.strip()]

with open('C:/laptrinhaaa/python học trên lớp/Python Kỳ 3/Btap/3.NumPy/weights_1.txt', 'r') as file:
    weight = [float(line.strip()) for line in file if line.strip()]


arr_height = np.array(height)
print("Bước 2 - arr_height:", arr_height)


arr_weight = np.array(weight)
print("Bước 3 - arr_weight:", arr_weight)


he_so_quy_doi_inch_sang_m = 0.0254
arr_height_m = arr_height * he_so_quy_doi_inch_sang_m
print("Bước 4 - arr_height_m:", arr_height_m)


he_so_quy_doi_pound_sang_kg = 0.453592
arr_weight_kg = arr_weight * he_so_quy_doi_pound_sang_kg
print("Bước 5 - arr_weight_kg:", arr_weight_kg)


arr_bmi = arr_weight_kg / (arr_height_m ** 2)
print("Bước 6 - arr_bmi:", arr_bmi)


if len(arr_weight_kg) > 50:
    can_nang_index_50 = arr_weight_kg[50]
    print("Bước 7 - Cân nặng tại vị trí index 50:", can_nang_index_50)
else:
    print("Bước 7 - Không thể lấy cân nặng tại vị trí index 50 vì mảng không đủ lớn.")


if len(arr_height_m) > 110:
    arr_height_m_100 = arr_height_m[100:111]
    print("Bước 8 - arr_height_m_100:", arr_height_m_100)
else:
    print("Bước 8 - Không thể lấy arr_height_m từ 100 đến 110 vì mảng không đủ lớn.")


cau_thu_bmi_duoi_21 = arr_bmi[arr_bmi < 21]
print("Bước 9 - Các cầu thủ có BMI < 21:", cau_thu_bmi_duoi_21)


chieu_cao_trung_binh = np.mean(arr_height_m)
can_nang_trung_binh = np.mean(arr_weight_kg)
print("Bước 10 - Chiều cao trung bình:", chieu_cao_trung_binh)
print("Bước 10 - Cân nặng trung bình:", can_nang_trung_binh)


chieu_cao_max = np.max(arr_height_m)
can_nang_max = np.max(arr_weight_kg)
print("Bước 11 - Chiều cao lớn nhất:", chieu_cao_max)
print("Bước 11 - Cân nặng lớn nhất:", can_nang_max)


chieu_cao_min = np.min(arr_height_m)
can_nang_min = np.min(arr_weight_kg)
print("Bước 12 - Chiều cao nhỏ nhất:", chieu_cao_min)
print("Bước 12 - Cân nặng nhỏ nhất:", can_nang_min)
