#Bài 6: Hiệu chỉnh lớp Stack bằng cách thêm vào hàm thành phần print để in nội dung của ngăn xếp
class Stack:
    def __init__(self, size):
        # Hàm tạo: khởi tạo một mảng với kích thước `size`
        self.stack = [0.0] * size  # Mảng kiểu float
        self.top = -1  # Chỉ số của phần tử trên cùng của ngăn xếp
        self.size = size  # Kích thước của ngăn xếp

    def isEmpty(self):
        # Kiểm tra ngăn xếp có trống không
        return self.top == -1

    def isFull(self):
        # Kiểm tra ngăn xếp đã đầy chưa
        return self.top == self.size - 1

    def push(self, value):
        # Đưa một phần tử vào ngăn xếp
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Đã đẩy {value} vào ngăn xếp.")

    def pop(self):
        # Lấy một phần tử ra từ đỉnh ngăn xếp
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử.")
            return None
        else:
            popped_value = self.stack[self.top]
            self.top -= 1
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    def count(self):
        # Trả về số phần tử hiện tại trên ngăn xếp
        return self.top + 1

    def print(self):
        # In nội dung ngăn xếp từ đỉnh xuống đáy
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp (từ đỉnh xuống đáy):")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def __del__(self):
        # Hàm hủy: dọn dẹp bộ nhớ khi đối tượng bị xóa
        print("Ngăn xếp đã bị hủy.")


# Chương trình chính
if __name__ == "__main__":
    # Tạo một ngăn xếp với kích thước 5
    s = Stack(5)

    # Thêm phần tử vào ngăn xếp
    s.push(1.1)
    s.push(2.2)
    s.push(3.3)

    # In nội dung của ngăn xếp
    s.print()

    # Lấy một phần tử ra khỏi ngăn xếp
    s.pop()

    # In lại nội dung ngăn xếp sau khi pop
    s.print()

    # Hủy đối tượng ngăn xếp
    del s