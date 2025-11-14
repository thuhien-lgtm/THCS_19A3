gia_san_pham = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
#Tổng chi phí
tong_chi_phi = gia_san_pham*so_luong
#Tổng phải trả: Tổng phải trả= tổng chi phí+(tổng cho phí*0.1)
tong_phai_tra = tong_chi_phi*1.1
print(f"Tổng tiền phải trả là: {tong_phai_tra:.2f}")
