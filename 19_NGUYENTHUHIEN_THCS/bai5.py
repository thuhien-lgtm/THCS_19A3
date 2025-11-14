tien_goc = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam_pt = float(input("Nhập lãi suất hàng năm (%): "))
lai_suat_nam = lai_suat_nam_pt / 100
lai_suat_quy = lai_suat_nam / 4
lai_suat_thang = lai_suat_nam / 12
lai_1_thang = tien_goc * lai_suat_thang * 1
lai_2_quy = tien_goc * lai_suat_quy * 2
lai_3_nam = tien_goc * lai_suat_nam * 3
print("Kết quả tính lãi đơn")
print(f"Tiền lãi sau 1 tháng: {lai_1_thang:.0f} VNĐ")
print(f"Tiền lãi sau 2 quý: {lai_2_quy:.0f} VNĐ")
print(f"Tiền lãi sau 3 năm: {lai_3_nam:.0f} VNĐ")
