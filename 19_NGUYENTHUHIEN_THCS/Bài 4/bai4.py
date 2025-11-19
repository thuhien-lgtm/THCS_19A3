def tim_so_nguyen_to(n):
    if n <= 2:
        return []
        # Tạo mảng boolean (is_prime[i] = True nếu i là nguyên tố)
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p) < n:
        if is_prime[p]:
            # Đánh dấu các bội số (bắt đầu từ p*p) là False
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1
        # Lọc ra danh sách các số nguyên tố
    so_nguyen_to = [p for p in range(2, n) if is_prime[p]]
    return so_nguyen_to