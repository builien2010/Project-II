
from nltk.stem import PorterStemmer  
from nltk.tokenize import sent_tokenize, word_tokenize  
  
stemmer = PorterStemmer()

example_words = ["wait", "a", "waited","waiting","waits"]  

array2 = []
for w in example_words:
    array2.append(stemmer.stem(w))
print(1)
print(array2)

'''
text = "I hate waiting in long lines. They waited at the train station together. The field marshal looks on and waits for letters addressed to him."  
tokenized = word_tokenize(text)  

print(stemmer.stem(words))  
'''