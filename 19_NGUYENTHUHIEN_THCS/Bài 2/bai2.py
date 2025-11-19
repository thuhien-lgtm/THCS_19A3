def tim_ucln(a, b):
    # Sử dụng giá trị tuyệt đối để xử lý số âm
    a = abs(a)
    b = abs(b)
    while b:
        # a sẽ nhận giá trị của b, b sẽ nhận giá trị của a % b (số dư)
        a, b = b, a % b 
    return a