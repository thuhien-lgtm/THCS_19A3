import os
dir_name = "temp_files"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Đã tạo thư mục: {dir_name}")
file_path = os.path.join(dir_name, "file.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Dữ liệu tạm thời.")
print(f"Đã tạo tập tin: {file_path}")
new_file_path = os.path.join(dir_name, "new_file.txt")
os.rename(file_path, new_file_path)
print(f"Đã đổi tên thành: {new_file_path}")
current_dir_path = "new_file.txt"
os.rename(new_file_path, current_dir_path)
print(f"Đã di chuyển tập tin ra thư mục hiện tại.")
os.rmdir(dir_name)
print(f"Đã xóa thư mục trống: {dir_name}")
print("\n--- Hoàn thành các bước của Bài 8! ---")