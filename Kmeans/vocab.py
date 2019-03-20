from sklearn.feature_extraction.text import CountVectorizer
from scipy import sparse, io

contents = []

f = open("train.txt", "r")


for line in f:
    
    line = line.rstrip()
    contents.append(line)

f.close()

print(len(contents))

vectorizer = CountVectorizer(min_df = 0.0005, max_df = 0.90)
X = vectorizer.fit_transform(contents)

io.mmwrite('train.mtx', X)


Y =  vectorizer.get_feature_names()
#print(Y)
#print(X)
print(len(Y))

f = open("vocab_train.txt", "w+")

vocab = ""
for i in Y:
    i = i + '\n'
    #print(i)
    vocab = vocab + i

f.write(vocab)

f.close()




    
