# 1. Khởi tạo và kết nối CSDL
#  Sử dụng SQLite3 để tạo và kết nối với cơ sở dữ liệu product.db
import sqlite3

# Kết nối hoặc tạo CSDL
conn = sqlite3.connect('product.db')

# Tạo con trỏ
cursor = conn.cursor()

# Tạo bảng product
cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
''')

conn.commit()
conn.close() 

# 2. Menu giao diện
 #  Tạo một menu đơn giản để người dùng lựa chọn chức năng.

def display_menu():
    print("=== Quản Lý Sản Phẩm ===")
    print("1. Hiển Thị Danh Sách Sản Phẩm")
    print("2. Thêm Sản Phẩm Mới")
    print("3. Tìm Kiếm Sản Phẩm Theo Tên")
    print("4. Cập Nhật Thông Tin Sản Phẩm")
    print("5. Xóa Sản Phẩm")
    print("6. Thoát")

#3. Chức năng chính
  #  Hiển thị danh sách sản phẩm
def display_products():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    if not products:
        print("Không có sản phẩm nào!")
    else:
        print("Danh sách sản phẩm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    
    conn.close()

   #. Thêm sản phẩm mới
def add_product():
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    conn.close()
    print("Thêm sản phẩm thành công!")

   # Tìm kiếm sản phẩm theo tên
def search_product():
    name = input("Nhập tên sản phẩm cần tìm: ")
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + name + '%',))
    products = cursor.fetchall()
    
    if not products:
        print("Không tìm thấy sản phẩm!")
    else:
        print("Kết quả tìm kiếm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    
    conn.close()

    #Cập nhật thông tin sản phẩm
def update_product():
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
    
    if cursor.rowcount == 0:
        print("Không tìm thấy sản phẩm!")
    else:
        print("Cập nhật thành công!")
    
    conn.commit()
    conn.close()

    # Xóa sản phẩm 
def delete_product():
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    
    if cursor.rowcount == 0:
        print("Không tìm thấy sản phẩm!")
    else:
        print("Xóa sản phẩm thành công!")
    
    conn.commit()
    conn.close()

# 4. Vòng lặp chính
def main():
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-6): ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
