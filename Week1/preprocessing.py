import re 
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer  
from nltk.tokenize import sent_tokenize, word_tokenize  
from sklearn.feature_extraction.text import CountVectorizer

def docFile(file):

    with open(file, "rb") as f:
        
        contents = f.read()

    contents = contents.decode('utf-8', 'ignore')

    f.close()

    # Tạo mảng array từ file : tách từ bằng khoảng trắng
    array = contents.split()

    # Loại bỏ các kí tự đặc biệt và số trong mỗi phần tử  trong mangr
    for i in range(0, len(array)):
        array[i] = array[i].lower() 
        array[i] = re.sub(r'[^a-z]', '', array[i])

    
    # Loại bỏ stopwords 

    array1 = []

    for word in array:
        if(word) not in (stopwords.words('english')):
            array1.append(word)


        
    # Stemming :

    stemmer = PorterStemmer()

    array2 = []
    stop = ['']
    for w in array1:
        if w not in stop:
            if( len(w) < 10):
                array2.append(stemmer.stem(w))

        
    #Conver list to String

    str = ' '.join(array2)
    return str

import os

path = "/media/builien/Study/Ki2Nam3/Project II/Week1/20_newsgroups"


FJoin = os.path.join
dirs = [FJoin(path, f) for f in os.listdir(path)]





vbs = []


for d in dirs:   
    files = [FJoin(d, f) for f in os.listdir(d)]
    for file in files:
        vb = docFile(file)
        vbs.append(vb)
           
print(vbs)

vectorizer = CountVectorizer()
print( vectorizer.fit_transform(vbs).todense() )
print( vectorizer.vocabulary_ )
