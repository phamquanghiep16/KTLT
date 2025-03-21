import math

def solve_quadratic(a, b, c):
    # Tính delta (biệt thức)
    delta = b**2 - 4*a*c
    
    # Kiểm tra các trường hợp
    if delta > 0:
        # Hai nghiệm phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    
    elif delta == 0:
        # Nghiệm kép
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    
    else:
        # Phương trình vô nghiệm
        return "Phương trình vô nghiệm (delta < 0)."

# Nhập hệ số từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra a có phải là 0 hay không
if a == 0:
    print("Không phải phương trình bậc 2 vì a = 0.")
else:
    # Giải phương trình
    result = solve_quadratic(a, b, c)
    print(result)
