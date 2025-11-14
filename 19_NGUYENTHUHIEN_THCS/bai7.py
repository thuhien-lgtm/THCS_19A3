ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")
if ten_dang_nhap == "admin" and mat_khau != "password123":
    print("Xác minh thành công!")
else:
    print("Xác minh không thành công!")
