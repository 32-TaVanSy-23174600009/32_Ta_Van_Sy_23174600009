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

    def __del__(self):
        # Hàm hủy: dọn dẹp bộ nhớ khi đối tượng bị xóa
        print("Ngăn xếp đã bị hủy.")


# Chương trình chính
if __name__ == "__main__":
    # Tạo một ngăn xếp với kích thước 5
    s = Stack(5)

    # Kiểm tra ngăn xếp rỗng
    print("Ngăn xếp có trống không?", s.isEmpty())

    # Thêm phần tử vào ngăn xếp
    s.push(1.1)
    s.push(2.2)
    s.push(3.3)
    s.push(4.4)
    s.push(5.5)

    # Kiểm tra ngăn xếp đầy
    print("Ngăn xếp có đầy không?", s.isFull())

    # Thử thêm phần tử vào ngăn xếp khi nó đã đầy
    s.push(6.6)

    # Lấy các phần tử ra khỏi ngăn xếp
    s.pop()
    s.pop()

    # Xóa đối tượng ngăn xếp
    del s