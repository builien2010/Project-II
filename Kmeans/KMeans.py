
from sklearn.cluster import KMeans 
from sklearn.feature_extraction.text import TfidfVectorizer 
from scipy import io
from sklearn import metrics

x_train = io.mmread("train1.mtx")

print("doc xong train1.txt")
print(x_train)

labels_true = []

f = open("label.txt", "r")

labels_true = [] 
data = f.read()
lines = data.split("\n")
for line in lines:
    #line = line.rstrip()
    #print(line)
    if( line != ' '):
        labels_true.append(line)
    
    

f.close()

#print("label:", labels_true)
del labels_true[-1]
#print(len(labels_true))

print("Khoi tao KMeans")
modelkmeans = KMeans(n_clusters = 20, init='k-means++', max_iter = 100, n_init = 7)

print("Chay Kmeans")
modelkmeans.fit(x_train)

print("chay xong Kmeans.")

labels_pred = modelkmeans.labels_

print(str(labels_pred))



#print("labels_pred", labels_pred)

c = metrics.adjusted_rand_score(labels_true, labels_pred)

print(c)

'''

x_test = io.mmread("test.mtx")


true_test_labels = ['alt.atheism', 
                    'comp.graphics', 
                    'comp.os.ms-windows.misc', 
                    'comp.sys.ibm.pc.hardware', 
                    'comp.sys.mac.hardware', 
                    'comp.windows.x',
                    'misc.forsale',
                    'rec.autos',
                    'rec.motorcycles',
                    'res.sport.baseball',
                    'res.sport.hockey',
                    'sci.crypt',
                    'sci.electronics',
                    'sci.med', 
                    'sci.space',
                    'soc.religion.christian',
                    'talk.politics.guns',
                    'talk.politics.mideast',
                    'talk.politics.misc',
                    'talk.religion.misc']

predicted_labels_kmeans = modelkmeans.predict(x_test)

print(predicted_labels_kmeans[0])

'''


