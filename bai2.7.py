import json 
#dữ liệu json (chuỗi)
json_data = '{"ten": "Sy","tuoi":19,"truong":"uneti"}'
#chuyển đổi Json thành đối tượng Python(dict)
Python_obj = json.loads(json_data)

#in đối tượng python
print(Python_obj)

#truy cập các giá trị trong đối tượng
print(Python_obj['ten'])
print(Python_obj['tuoi'])
