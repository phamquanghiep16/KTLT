# Hàm in ra số nghịch đảo và kết quả dưới dạng thập phân của các số trong dãy từ a đến b
def print_inverse_and_decimal(a, b):
    for num in range(a, b + 1):
        # Tính số nghịch đảo
        inverse = 1 / num
        # In kết quả
        print(f"Số: {num}, Nghịch đảo: {inverse}, Kết quả dưới dạng thập phân: {format(inverse, '.6f')}")

# Nhập giá trị a và b
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

# Gọi hàm để in kết quả
print_inverse_and_decimal(a, b)
