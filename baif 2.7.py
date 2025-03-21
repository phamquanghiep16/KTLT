# Yêu cầu người dùng nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# Tạo dictionary với các cặp (i, i*i)
squares_dict = {i: i*i for i in range(1, n+1)}

# In ra dictionary
print(squares_dict)
