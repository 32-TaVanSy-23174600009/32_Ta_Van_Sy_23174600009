import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Tạo hoặc kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Tạo bảng sản phẩm nếu chưa có
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')
conn.commit()

# Hàm thêm sản phẩm
def add_product():
    name = name_entry.get()
    price = price_entry.get()
    if not name or not price:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    try:
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, float(price)))
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm sản phẩm thành công!")
        update_product_list()
    except ValueError:
        messagebox.showerror("Lỗi", "Giá phải là một số hợp lệ!")

# Hàm cập nhật danh sách sản phẩm
def update_product_list():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM products")
    for product in cursor.fetchall():
        tree.insert("", "end", values=product)

# Hàm tìm kiếm sản phẩm
def search_product():
    query = name_entry.get()
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{query}%",))
    for product in cursor.fetchall():
        tree.insert("", "end", values=product)

# Hàm xóa sản phẩm
def delete_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm để xóa!")
        return
    product_id = tree.item(selected_item[0])['values'][0]
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    messagebox.showinfo("Thành công", "Xóa sản phẩm thành công!")
    update_product_list()

# Hàm cập nhật sản phẩm
def update_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm để cập nhật!")
        return
    product_id = tree.item(selected_item[0])['values'][0]
    name = name_entry.get()
    price = price_entry.get()
    if not name or not price:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    try:
        cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (name, float(price), product_id))
        conn.commit()
        messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công!")
        update_product_list()
    except ValueError:
        messagebox.showerror("Lỗi", "Giá phải là một số hợp lệ!")

# Tạo giao diện
root = tk.Tk()
root.title("Quản lý Sản phẩm")

# Labels và Entries
name_label = tk.Label(root, text="Tên sản phẩm:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

price_label = tk.Label(root, text="Giá:")
price_label.grid(row=1, column=0, padx=10, pady=10)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons
add_button = tk.Button(root, text="Thêm", command=add_product)
add_button.grid(row=2, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="Tìm kiếm", command=search_product)
search_button.grid(row=2, column=1, padx=10, pady=10)

update_button = tk.Button(root, text="Cập nhật", command=update_product)
update_button.grid(row=3, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Xóa", command=delete_product)
delete_button.grid(row=3, column=1, padx=10, pady=10)

# Treeview để hiển thị danh sách sản phẩm
tree = ttk.Treeview(root, columns=("ID", "Tên sản phẩm", "Giá"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Tên sản phẩm", text="Tên sản phẩm")
tree.heading("Giá", text="Giá")
tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Cập nhật danh sách sản phẩm ban đầu
update_product_list()

# Chạy ứng dụng
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát
conn.close()
