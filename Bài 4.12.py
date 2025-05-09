print("Phạm Quang Hiệp")
print("MSSV: 23575202071001")
print("#####################")
ds = input("Nhập chuỗi: ")
ds = ds.split()

ds = [int(x.strip()) for x in ds]

ds = [x for x in ds if x != 123]

print("Danh sách sau khi loại bỏ phần tử 123:")
print(ds)
