import numpy as np

#  1
with open('C:/laptrinhaaa/python học trên lớp/Python Kỳ 3/Btap/3.NumPy/baseball_2D.txt', 'r') as file:
    baseball = [list(map(float, line.strip().split())) for line in file if line.strip()]

# Tạo mảng numpy 2D từ danh sách baseball
np_baseball = np.array(baseball)
print(" 1 - Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
print(" 1 - Kích thước của np_baseball:", np_baseball.shape)

#  2
if np_baseball.shape[0] > 50:
    print("\n 2 - Các giá trị của dòng thứ 50:", np_baseball[49])
else:
    print("\n 2 - Không có dòng thứ 50 trong dữ liệu.")

#  3
np_weight = np_baseball[:, 1]
print("\n 3 - np_weight (cân nặng của các cầu thủ):", np_weight)

#  4
if np_baseball.shape[0] > 124:
    chieu_cao_vd_124 = np_baseball[123, 0]
    print("\n 4 - Chiều cao của vận động viên thứ 124:", chieu_cao_vd_124)
else:
    print("\n 4 - Không có vận động viên thứ 124 trong dữ liệu.")

#  5
chieu_cao_trung_binh = np.mean(np_baseball[:, 0])
can_nang_trung_binh = np.mean(np_weight)
print("\n 5 - Chiều cao trung bình của các cầu thủ:", chieu_cao_trung_binh)
print(" 5 - Cân nặng trung bình của các cầu thủ:", can_nang_trung_binh)

#  6
correlation = np.corrcoef(np_baseball[:, 0], np_weight)[0, 1]
if correlation > 0:
    relation = "tương quan thuận"
elif correlation < 0:
    relation = "tương quan nghịch"
else:
    relation = "không có tương quan"
print("\n 6 - Hệ số tương quan giữa chiều cao và cân nặng:", correlation)
print(" 6 - Nhận xét: Mối tương quan giữa chiều cao và cân nặng là", relation)
