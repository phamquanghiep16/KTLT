print("Phạm Quang Hiệp")
print("MSSV:23575202071001")
print("#####################")
result = []
for num in range(1000, 3001):
    digits = [int(digit) for digit in str(num)]  
    if all(digit % 2 == 0 for digit in digits):  
        result.append(str(num))  
print(",".join(result))
