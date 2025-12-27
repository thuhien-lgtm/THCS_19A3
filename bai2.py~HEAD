content = """Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng. Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, trí tuệ nhân tạo và tự động hóa. Cộng đồng Python rất lớn và hỗ trợ tuyệt vời, với nhiều thư viện phong phú để giải quyết mọi vấn đề."""
with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write(content)
with open("vanban.txt", "r", encoding="utf-8") as f:
    data = f.read()
data_clean = data.lower().replace(",", "").replace(".", "")
words = data_clean.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f"{'Từ':<15} | {'Số lần xuất hiện'}")
print("-" * 35)
for word, count in word_count.items():
    print(f"{word:<15} | {count}")