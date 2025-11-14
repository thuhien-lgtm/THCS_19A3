so_kWh = float(input("Số kWh đã tiêu thụ: "))
if so_kWh < 0 :
    print("Số kWh không hợp lệ!")
elif so_kWh > 0 and so_kWh < 100  :
    don_gia = 1.678
elif so_kWh > 101 and so_kWh < 200  :
    don_gia = 1.734
elif so_kWh > 201 and so_kWh < 300 :
    don_gia = 2.104
if so_kWh > 0 :
    tien_dien = so_kWh * don_gia
    print (f"Tổng số điện phải trả là: {tien_dien:.0f} VND")
