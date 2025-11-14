nam = int(input("Nhập năm: "))
dieu_kien_1 = (nam % 400 == 0)
dieu_kien_2 = (nam %4 == 0) and (nam % 100 != 0)
if (dieu_kien_1 or dieu_kien_2):
    print ("Năm {nam} là năm nhuận")
else:
    print ("Năm {nam} không là năm nhuận")
