
import os

path = "/media/builien/Study/Ki2Nam3/Project II/Week1/20_newsgroups"


print(os.listdir(path))

#dir = os.listdir(path)

FJoin = os.path.join
dirs = [FJoin(path, f) for f in os.listdir(path)]
print(dirs)

# Mảng 2 chiều lưu các file
path_file = []
for d in dirs:
    files = [FJoin(d, f) for f in os.listdir(d)]
    print(files)
    path_file.append(files)
print(path_file)
print(len(path_file))



    