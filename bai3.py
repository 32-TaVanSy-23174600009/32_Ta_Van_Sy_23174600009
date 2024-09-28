class PS:
    def __init__(self,tu_so,mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
        
    def kiem_tra(self):
        return self.mau_so != 0
    
    def nhap_phan_so(self):
        self.tu_so = int(input("nhap tu so"))
        self.mau_so = int(input("nhập mẫu số"))

    def in_phan_so(self):
        print(f"{self.tu_so}/{self.mau_so}")

#ví dụ
phan_so = PS(3,4)
phan_so.in_phan_so()

    
    # Nhập phân số từ người dùng
phan_so.nhap_phan_so()
phan_so.in_phan_so()