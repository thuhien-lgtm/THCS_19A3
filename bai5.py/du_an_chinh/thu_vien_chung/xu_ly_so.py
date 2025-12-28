<<<<<<< HEAD:19_NGUYENTHUHIEN_THCS/bài 5/thu_vien_chung/xu_ly_so.py
def kiem_tra_so_nguyen_to(so):
    if so < 2: return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0: return False
=======
import math
def kiem_tra_so_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, int(math.sqrt(so)) + 1):
        if so % i == 0:
            return False
>>>>>>> 8d4864fb6813d8db8fe06155f0380d4f1b48049b:bai5.py/du_an_chinh/thu_vien_chung/xu_ly_so.py
    return True