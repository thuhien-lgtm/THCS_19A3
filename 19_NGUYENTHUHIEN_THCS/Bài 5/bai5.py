def tinh_cac_tong(n):
    if n < 1:
        return "n phải là số nguyên dương."
    # 1. Tính S1
    S1 = n * (n + 1) // 2
    # 2. Tính S2 = (n-1)!
    S2 = 1
    if n > 1:
        for i in range(1, n):
            S2 *= i
    # 3. Tính S3: Tổng xen kẽ
    S3 = 0.0
    for i in range(1, n + 1):
        if i % 2 == 1:
            S3 += 1.0 / i
        else:
            S3 -= 1.0 / i
    # 4. Tính S4: Tổng Sigma
    S4 = 0.0
    for k in range(n + 1):
        # Lưu ý: k=0, số hạng là 0/(0+2) = 0
        S4 += k / (k + 2)
    return (
        f"S1 = {S1}\n"
        f"S2 = {S2}\n"
        f"S3 = {S3:.6f}\n"
        f"S4 = {S4:.6f}" )
    