import csv
header = ['ID', 'Tên', 'Lương']
data = [
    ['1', 'Nguyễn Văn A', '45000'],
    ['2', 'Trần Thị B', '60000'],
    ['3', 'Lê Văn C', '55000']
]
with open('nhan_vien.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
print("\n--- Nhân viên có lương > 50000 ---")
with open('nhan_vien.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Lương']) > 50000:
            print(f"Tên: {row['Tên']} - Lương: {row['Lương']}")