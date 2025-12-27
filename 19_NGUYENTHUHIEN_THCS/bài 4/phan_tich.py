from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri
ds_so = [15, 3, 9, 22, 1]
ds_da_sap_xep = sap_xep_tang_dan(ds_so)
print(f"Danh sách sau khi sắp xếp: {ds_da_sap_xep}")
my_dict = {"ten": "Python", "phien_ban": 3.12, "loai": "Lap trinh"}
key = "phien_ban"
print(f"Giá trị của '{key}' là: {lay_gia_tri(my_dict, key)}")