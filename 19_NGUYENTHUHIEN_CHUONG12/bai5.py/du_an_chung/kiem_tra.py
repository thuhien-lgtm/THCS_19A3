import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'thu_vien_chung'))
sys.path.append(path)
import xu_ly_so
n = 17
print(f"Số {n} là số nguyên tố: {xu_ly_so.kiem_tra_so_nguyen_to(n)}")