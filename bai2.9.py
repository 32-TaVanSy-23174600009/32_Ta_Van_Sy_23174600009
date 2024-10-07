import json

# Đối tượng từ điển Python mẫu
data ='{"ten": "Sy","tuoi":19,"truong":"uneti"}'

# Sắp xếp từ điển theo khóa
sorted_data = {key: data[key] for key in sorted(data.keys())}

# Chuyển đổi đối tượng từ điển thành chuỗi JSON
json_string = json.dumps(sorted_data, ensure_ascii=False, indent=4)

# In ra chuỗi JSON với thụt lề 4
print("Chuỗi JSON:")
print(json_string)

# In ra tất cả các thành viên trong đối tượng với mức thụt lề 4
print("\nCác thành viên trong đối tượng:")
for key, value in sorted_data.items():
    print(f"{key}: {json.dumps(value, ensure_ascii=False, indent=4)}")