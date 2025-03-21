a = "Hello Guy!"  # Biến toàn cục

def say(a):  # Biến a trong hàm là cục bộ
    a = "Vinh University"  # Biến a trong hàm sẽ chỉ ảnh hưởng đến phạm vi hàm
    print(a)  # In giá trị của a trong hàm (Vinh University)

# In giá trị của a ngoài hàm (Hello Guy!)
print(a)

# Gọi hàm say
say(a)

# In giá trị của a ngoài hàm sau khi gọi hàm (Hello Guy!)
print(a)
