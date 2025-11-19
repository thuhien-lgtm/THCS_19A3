import math
def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    # Lấy phần nguyên của căn bậc hai
    can_nguyen = math.isqrt(n) 
     # Kiểm tra lại bình phương
    return can_nguyen * can_nguyen == n