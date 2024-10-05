from xml.dom import minidom

# Tải file XML
file_path = 'sample.xml'
doc = minidom.parse(file_path)

# Lấy tên công ty
company_name = doc.getElementsByTagName('name')[0].firstChild.nodeValue
print(f"Công ty: {company_name}")

# Lấy danh sách nhân viên
staff_list = doc.getElementsByTagName('staff')
for staff in staff_list:
    staff_id = staff.getAttribute('id')
    staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.nodeValue
    print(f"Nhân viên ID: {staff_id}, Tên: {staff_name}, Lương: {staff_salary}")