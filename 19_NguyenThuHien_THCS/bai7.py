lst = [1, 4, 3, 2, 5, 0, 6, 7]
tong_muc_tieu = 7
print(f"Các cặp số có tổng bằng {tong_muc_tieu} là:")
n = 0
for _ in lst:
    n += 1  
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] + lst[j] == tong_muc_tieu:
            print(f"({lst[i]}, {lst[j]})")