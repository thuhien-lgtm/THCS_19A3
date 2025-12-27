import sys
import os
duong_dan_thu_vien = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'thu_vien_chung'))
sys.path.append(duong_dan_thu_vien)
import xu_ly_so
n = 17
if xu_ly_so.kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")