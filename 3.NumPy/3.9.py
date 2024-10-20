import pandas as pd


euro12 = pd.read_csv('C:/laptrinhaaa/python học trên lớp/Python Kỳ 3/Btap/3.NumPy/euro2012.csv')


print("Bước 1 - Thông tin DataFrame:")
print("Kiểu dữ liệu của euro12:", type(euro12))
print("Kích thước của euro12:", euro12.shape)
print("Tên các cột trong euro12:", euro12.columns.tolist())


print("\nBước 2 - Giá trị cột Goals:")
print(euro12['Goals'])


so_doi_tham_gia = euro12['Team'].nunique()
print("\nBước 3 - Số đội tham gia Euro 2012:", so_doi_tham_gia)


print("\nBước 4 - Thông tin của Euro2012:")
print(euro12.info())


discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\nBước 5 - DataFrame discipline:")
print(discipline)


discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print("\nBước 6 - Discipline sắp xếp giảm dần theo 'Red Cards' và 'Yellow Cards':")
print(discipline_sorted)


trung_binh_yellow_cards = discipline['Yellow Cards'].mean()
print("\nBước 7a - Trung bình số thẻ vàng:", trung_binh_yellow_cards)


doi_ghi_hon_6_ban = euro12[euro12['Goals'] > 6]
print("\nBước 7b - Các đội ghi hơn 6 bàn thắng:")
print(doi_ghi_hon_6_ban[['Team', 'Goals']])


doi_bat_dau_bang_G = euro12[euro12['Team'].str.startswith('G')]
print("\nBước 8 - Các đội mà tên bắt đầu bằng 'G':")
print(doi_bat_dau_bang_G['Team'])


print("\nBước 9 - 7 cột đầu của euro12:")
print(euro12.iloc[:, :7])


print("\nBước 10 - Tất cả các cột, trừ 3 cột cuối:")
print(euro12.iloc[:, :-3])


print("\nBước 11 - Các cột 'Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards':")
print(euro12[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])


doi_chon = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]
print("\nBước 12 - Các cột 'Team' và 'Shooting Accuracy' từ 'England', 'Italy', 'Russia':")
print(doi_chon[['Team', 'Shooting Accuracy']])
