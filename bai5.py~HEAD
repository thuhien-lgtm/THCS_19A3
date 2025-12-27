content = "ID, Tên sản phẩm, Giá\n1, Laptop, 1200\n2, Chuột máy tính, 25\n3, Bàn phím, 75"
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write(content)
source_file = "san_pham.txt"
dest_file = "san_pham_copy.txt"
with open(source_file, "rb") as f_src, open(dest_file, "wb") as f_dst:
    while True:
        chunk = f_src.read(1024)
        if not chunk:
            break
        f_dst.write(chunk)
print(f"Đã sao chép thành công từ '{source_file}' sang '{dest_file}'!")