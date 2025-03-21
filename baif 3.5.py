a = "Hello Guy!"  # Biến toàn cục

def say():
    global a  # Sử dụng biến toàn cục 'a'
    a = "Vinh University"  # Thay đổi giá trị của biến a toàn cục
    print(a)  # In giá trị của biến a trong hàm

# Gọi hàm say
say()

# In giá trị của a sau khi thay đổi trong hàm
print(a)
