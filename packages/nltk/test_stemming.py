# test_stemming.py
from nltk.stem import PorterStemmer

ps = PorterStemmer()

text = ["python","pythoner","pythoning","pythoned","pythonly"]
for word in text:
    print( ps.stem(word) )

from nltk.tokenize import word_tokenize

sentence = "Stemming finds the origin of a word; writ is the stem of the forms writing and written."
words = word_tokenize(sentence)

for word in words:
    print( word," ", ps.stem(word))

# To clean up some stop words,
from nltk.corpus import stopwords

print("--------------------------------------")
stop_words = set( stopwords.words("english"))
for word in words:
    if word not in stop_words:
        print( word," ", ps.stem(word))
