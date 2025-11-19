def rut_gon_phan_so(tu_so, mau_so):
    if mau_so == 0:
        return None, "Lỗi: Mẫu số bằng 0"
    # Tìm UCLN của giá trị tuyệt đối
    ucln = tim_ucln(tu_so, mau_so)
    tu_toi_gian = tu_so // ucln
    mau_toi_gian = mau_so // ucln
    # Đảm bảo mẫu số dương: nếu mẫu âm, chuyển dấu lên tử
    if mau_toi_gian < 0:
        tu_toi_gian = -tu_toi_gian
        mau_toi_gian = -mau_toi_gian
    return tu_toi_gian, mau_toi_gian