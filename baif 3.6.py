def get_sum(*num):
    tmp = 0
    # Duyệt qua các tham số
    for i in num:
        tmp += i
    return tmp

# Gọi hàm với các tham số
result = get_sum(1, 2, 3, 4, 5)
print(result)
