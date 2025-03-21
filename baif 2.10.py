# Nhập xâu ký tự từ bàn phím
input_string = input("Nhập xâu ký tự: ")

# Tách xâu thành danh sách các từ bằng phương thức split()
words = input_string.split()

# In ra danh sách các từ
print("Danh sách các từ sau khi tách:", words)

# Nối lại các từ thành một xâu mới, sử dụng dấu cách làm phân cách giữa các từ
new_string = " ".join(words)

# In ra xâu đã nối lại
print("Xâu đã nối lại:", new_string)
