luong_co_ban = float(input("Nhập lương cơ bản (VND): "))
so_ngay_cong = int(input("Nhập số ngày công: "))
luong_mot_ngay = luong_co_ban / 22
luong_chinh = luong_mot_ngay * so_ngay_cong
tien_thuong = 0
tien_phat = 0
if so_ngay_cong > 22:
    tien_thuong = luong_chinh * 0.1
elif so_ngay_cong < 22:
    tien_phat = luong_chinh *0.05
luong_nhan_duoc = luong_chinh + tien_thuong - tien_thuong
print("Bảng lương")
print(f"Lương chính: {luong_chinh} VND")
print(f"Tiền thưởng: {tien_thuong} VND")
print(f"Tiền phạt: {tien_phat} VND")
print(f"Lương nhận được: {luong_nhan_duoc}")
