import re 
import numpy as np 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer  
from nltk.tokenize import sent_tokenize, word_tokenize  
from sklearn.feature_extraction.text import CountVectorizer


def docFile(file1):

    print(file1)
    with open(file1, "rb") as f:
        
        contents = f.read()

        contents = contents.decode('utf-8', 'ignore')

    f.close()

    # Tạo mảng array từ file : tách từ bằng khoảng trắng
    arrays = contents.split()
    #print("B1: len = ", len(array))

    # Loại bỏ các kí tự đặc biệt và số trong mỗi phần tử  trong mangr
    array1 = []
    stemmer = PorterStemmer()
    for word in arrays:
        word = word.lower() 
        word = re.sub(r'[^a-z]', '', word)
        if(word) not in (stopwords.words('english')):
            if( len(word) < 10 and len(word) > 2):
                array1.append(stemmer.stem(word))
    
    tf = np.unique(array1, return_counts = True)[1].tolist()
    value = np.unique(array1, return_counts = True)[0].tolist()

    str = ' '.join(value)
    

    return str


import os
path1 = "/media/builien/Study/Ki2Nam3/Project II/week3/20news-bydate/20news-bydate-train"
path2 = "/media/builien/Study/Ki2Nam3/Project II/week3/20news-bydate/20news-bydate-test"

FJoin = os.path.join
def solve(path):
    contents = ""

    dirs = [FJoin(path, f) for f in os.listdir(path)]

    for i in range(0,len(dirs)): 
        d = dirs[i]  
        files = [FJoin(d, f) for f in os.listdir(d)]
        for j in range(0,len(files)):
        
            s = docFile(files[j])
            #print(str)
            s = str(i) + "<###>" +  s + "\n"
            contents = contents + s

    return contents
                

contents_train = solve(path1)

file = open("train.txt", "w+")
file.write(contents_train)
file.close()

contents_test = solve(path2)
file = open("test.txt", "w+")
file.write(contents_test)
file.close()




