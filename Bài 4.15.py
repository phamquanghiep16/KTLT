print("Phạm Quang Hiệp")
print("MSSV:235752020710015")
print("#####################")
input_str = input("Nhập chuỗi các từ tiếng Anh: ")
words = input_str.split()
words.sort()
print("Các từ theo thứ tự từ điển là:")
for word in words:
    print(word)
