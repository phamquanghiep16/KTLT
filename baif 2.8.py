# Khởi tạo hai số đầu tiên của dãy Fibonacci
a, b = 0, 1

# Khởi tạo biến để tính tổng các số chẵn
even_sum = 0

# In ra các số Fibonacci nhỏ hơn 4.000.000 và tính tổng các số chẵn
while b < 4000000:
    # Nếu số Fibonacci là chẵn, cộng vào tổng
    if b % 2 == 0:
        even_sum += b
    
    # In ra số Fibonacci (tuỳ chọn, nếu bạn muốn in ra dãy số)
    print(b, end=' ')
    
    # Cập nhật các số Fibonacci
    a, b = b, a + b

# In ra tổng các số chẵn
print("\nTổng các số chẵn trong dãy Fibonacci:", even_sum)
