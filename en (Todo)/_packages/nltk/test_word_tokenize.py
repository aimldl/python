# test_tokenize.py
# First, run the following commands in IPYTHON.
# import nltk
# nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hi, there. How are you doing? NLTK is a great tool to learn about NLP."
print( sent_tokenize(text) )    # Tokenize sentence
print( word_tokenize(text) )    # Tokenize word

for word in word_tokenize(text):
    print(word)