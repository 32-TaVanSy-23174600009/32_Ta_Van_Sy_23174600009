import xml.etree.ElementTree as ET

# Chuỗi XML
xml_string = '''<?xml version="1.0"?>
<company>
    <name>GeeksForGeeks Company</name>
    <staff id="1">
        <name>Amar Pandey</name>
        <salary>8.5 LPA</salary>
    </staff>
    <staff id="2">
        <name>Akbhar Khan</name>
        <salary>6.5 LPA</salary>
    </staff>
    <staff id="3">
        <name>Anthony Walter</name>
        <salary>3.2 LPA</salary>
    </staff>    
</company>'''

# Phân tích cú pháp chuỗi XML
root = ET.fromstring(xml_string)

# Lấy danh sách các phần tử 'staff'
staff_list = root.findall('staff')

# In ra tên của từng phần tử
for staff in staff_list:
    name = staff.find('name').text
    print(name)