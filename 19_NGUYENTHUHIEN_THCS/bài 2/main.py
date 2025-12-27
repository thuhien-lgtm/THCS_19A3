from chuoi_utility import dao_nguoc_chuoi
van_ban = "Chào mừng bạn đến với Python"
ket_qua = dao_nguoc_chuoi(van_ban)
print(f"Chuỗi ban đầu: {van_ban}")
print(f"Chuỗi sau khi đảo ngược: {ket_qua}")