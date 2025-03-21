import re

def check_password_validity(password):
    # Kiểm tra xem mật khẩu có ít nhất một chữ cái thường
    if not re.search(r'[a-z]', password):
        return "Mật khẩu phải có ít nhất một chữ cái thường (a-z)."
    
    # Kiểm tra xem mật khẩu có ít nhất một chữ cái hoa
    if not re.search(r'[A-Z]', password):
        return "Mật khẩu phải có ít nhất một chữ cái hoa (A-Z)."
    
    # Kiểm tra xem mật khẩu có ít nhất một số
    if not re.search(r'[0-9]', password):
        return "Mật khẩu phải có ít nhất một số (0-9)."
    
    # Nếu tất cả các điều kiện đều thỏa mãn
    return "Mật khẩu hợp lệ!"

# Nhập mật khẩu từ người dùng
password = input("Nhập mật khẩu: ")
result = check_password_validity(password)
print(result)
