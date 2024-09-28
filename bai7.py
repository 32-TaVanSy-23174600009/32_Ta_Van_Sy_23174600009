class Date:
    def __init__(self, day=1, month=1, year=1900):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        # Số ngày trong từng tháng
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 
                         31, 31, 30, 31, 30, 31]
        
        self.day += 1
        
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            
            if self.month > 12:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        # Kiểm tra năm nhuận
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)


# Ví dụ sử dụng lớp Date
date = Date(28, 2, 2020)
date.display()  # In ra: 28/02/2020
date.next()
date.display()  # In ra: 29/02/2020
date.next()
date.display()  # In ra: 01/03/2020