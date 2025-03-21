# Nhập xâu ký tự từ bàn phím
input_string = input("Nhập xâu ký tự: ")

# Khởi tạo từ điển để đếm số lần xuất hiện của từng ký tự
char_count = {}

# Duyệt qua từng ký tự trong xâu
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# In ra từ điển chứa các ký tự và số lần xuất hiện
print("Số lần xuất hiện của các ký tự trong xâu:")
print(char_count)
