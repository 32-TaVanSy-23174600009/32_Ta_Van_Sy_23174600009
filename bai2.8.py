import json

#Đối tượng Python
data = {
    "name": "Tạ Văn Sỹ",
    "age":20,
    "truong":"uneti"
}
#Chuyển đối tượng Python thành chuõi json 
json_string= json.dumps(data)

json_string1=json.dumps(data,ensure_ascii=False)

print(json_string)
print(json_string1)

print(type(json_string))