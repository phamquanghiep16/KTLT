# Khởi tạo danh sách lưu các số thỏa mãn điều kiện
result = []

# Duyệt qua các số trong khoảng từ 2000 đến 3200
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))

# In kết quả dưới dạng chuỗi, các số cách nhau bởi dấu phẩy
print(", ".join(result))
