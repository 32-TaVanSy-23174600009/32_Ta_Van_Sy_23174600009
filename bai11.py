class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh thứ nhất
        self.b = b  # Cạnh thứ hai
        self.c = c  # Cạnh thứ ba

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Sử dụng công thức Heron để tính diện tích
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

class IsoscelesTriangle(Triangle):
    def __init__(self, base, height):
        self.base = base  # Cạnh đáy
        self.height = height  # Chiều cao
        # Cạnh bên (c) được tính từ chiều cao và cạnh đáy
        side = (base / 2) ** 2 + height ** 2  # Tính cạnh bên
        super().__init__(base, side ** 0.5, side ** 0.5)  # Gọi hàm khởi tạo của lớp Triangle

    def area(self):
        return (self.base * self.height) / 2

class RightTriangle(Triangle):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.hypotenuse = (base ** 2 + height ** 2) ** 0.5
        super().__init__(base, height, self.hypotenuse)

    def area(self):
        return (self.base * self.height) / 2

class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        super().__init__(side, (side * (3 ** 0.5)) / 2)  # Tính chiều cao của tam giác đều

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tam giác vuông
    base = float(input("Nhập chiều dài cạnh đáy của tam giác vuông: "))
    height = float(input("Nhập chiều cao của tam giác vuông: "))
    right_triangle = RightTriangle(base, height)
    print(f"Chu vi tam giác vuông: {right_triangle.perimeter()}")
    print(f"Diện tích tam giác vuông: {right_triangle.area()}")

    # Tam giác cân
    base = float(input("Nhập chiều dài cạnh đáy của tam giác cân: "))
    height = float(input("Nhập chiều cao của tam giác cân: "))
    isosceles_triangle = IsoscelesTriangle(base, height)
    print(f"Chu vi tam giác cân: {isosceles_triangle.perimeter()}")
    print(f"Diện tích tam giác cân: {isosceles_triangle.area()}")

    # Tam giác đều
    side = float(input("Nhập chiều dài cạnh của tam giác đều: "))
    equilateral_triangle = EquilateralTriangle(side)
    print(f"Chu vi tam giác đều: {equilateral_triangle.perimeter()}")
    print(f"Diện tích tam giác đều: {equilateral_triangle.area()}")