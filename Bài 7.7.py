print("Phạm Quang Hiệp")
print("MSSV: 235752020710015")
print("#####################")
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        return "File không tồn tại"

file_path = "D:/a.txt"
print("Số dòng trong tệp là:", count_lines(file_path))

