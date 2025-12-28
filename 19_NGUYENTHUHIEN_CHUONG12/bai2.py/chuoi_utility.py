def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
def dem_so_tu(chuoi):
    danh_sach_tu = chuoi.split()
    return len(danh_sach_tu)