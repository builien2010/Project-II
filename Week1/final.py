import re 
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer  
from nltk.tokenize import sent_tokenize, word_tokenize  
  


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



    
# Đọc file 49960 

with open("49960", "rb") as f:
    contents = f.read()

contents = contents.decode('utf-8', 'ignore')


# Tạo mảng array từ file : tách từ bằng khoảng trắng
array = contents.split()


f.close()
'''

f = open("array.txt", "wb")

f.write(array)

f.close()



for i in range(0, len(array)):
    #print(a,x)
    #print(type(a))
    array[i] = array[i].lower()


print(array)
#print(len(array))

'''

# Loại bỏ các kí tự đặc biệt và số trong mỗi phần tử  trong mangr
for i in range(0, len(array)):
    #print(a,x)
    #print(type(a))
    array[i] = array[i].lower() 
    array[i] = re.sub(r'[^a-z]', '', array[i])

print(array)
print(len(array))

# Loại bỏ stopwords 

array1 = []

for word in array:
    if(word) not in (stopwords.words('english')):
        array1.append(word)

print(array1)
print(len(array1))
 
# Stemming :

stemmer = PorterStemmer()

array2 = []
stop = ['']
for w in array1:
    if w not in stop:
        array2.append(stemmer.stem(w))

print(array2)
print(len(array2))

