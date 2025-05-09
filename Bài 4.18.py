print("Phạm Quang Hiệp")
print("MSSV:23575202071001")
print("#####################")
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("Nhập số nguyên n: "))
fibonacci_list = fibonacci(n)
print("Các số Fibonacci nhỏ hơn", n, "là:", fibonacci_list)
