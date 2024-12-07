# test_stop_words.py
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
#print(stop_words)

text = "The second text is to show how to filter out stop words with NLTK."
#print( text )

words = word_tokenize(text)
print(words)

filtered_text = []
for word in words:
    if word not in stop_words:
        filtered_text.append(word) 

print(filtered_text)

# https://en.wikipedia.org/wiki/Stop_words
text_02 = "According to Wikipedia, stop words are words which are filtered out \
before or after processing of natural language data (text). Though \
stop words usually refers to the most commond words in a language, \
there is no single universal list of stop words used by all NLP tools, \
and indeed not all tools even use such a list. Some tools \
specifically avoid removing these stop words to support phrase search."

words_02 = word_tokenize(text_02)
print(words_02)

# The following line does the same filteration in one sentence.
filtered_text = [word for word in words_02 if not word in stop_words]
print(filtered_text)