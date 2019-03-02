from nltk.corpus import stopwords

'''
text = 'hello bye the the hi a a an the'
text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])

print(text)
'''

array = ['aaa', 'a', 'hello']

print(1)
array1 = []

for word in array:
    if(word) not in (stopwords.words('english')):
        array1.append(word)

print(array1)