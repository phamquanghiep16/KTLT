print("Phạm Quang Hiệp")
print("MSSV:23575202071001")
print("#####################")
def read_last_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1]
        return last_line

file_path = 'D:/a.txt'

last_line = read_last_line(file_path)
print(last_line.strip())
