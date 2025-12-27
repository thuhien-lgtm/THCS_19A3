content = """ID, Tên sản phẩm, Giá
1, Laptop, 1200
2, Chuột máy tính, 25
3, Bàn phím, 75"""
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write(content)
id_update = input("Nhập ID của sản phẩm cần cập nhật giá: ")
new_price = input("Nhập giá mới: ")
updated_data = []
with open("san_pham.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    header = lines[0]
    updated_data.append(header)
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        if parts[0] == id_update:
            parts[2] = new_price
        new_line = ", ".join(parts) + "\n"
        updated_data.append(new_line)
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.writelines(updated_data)
print("Cập nhật giá thành công!")