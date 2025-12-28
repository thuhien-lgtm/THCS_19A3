import os
folders = ['my_project/src', 'my_project/docs', 'my_project/data']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
files = [
    'my_project/src/main.py',
    'my_project/docs/README.md',
    'my_project/data/input.txt'
]
for file_path in files:
    with open(file_path, 'w', encoding='utf-8') as f:
        pass 
print("\n--- Cấu trúc thư mục my_project ---")
for root, dirs, files in os.walk('my_project'):
    print(f"Thư mục: {root}")
    for file in files:
        print(f"  - File: {file}")