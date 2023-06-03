# test_pos_tagging.py

# This directory for reuters didn't exist, but the corresponding zip file does.
# So I unzipped and made a directory. 
# Doing so and importing like below simply doesn't work.
#from nltk.corpus.reuters import reuters
from nltk.corpus import PlaintextCorpusReader

corpus_root = 'C:/Users/phil4/AppData/Roaming/nltk_data/corpora/reuters/test'
document = PlaintextCorpusReader(corpus_root,'14826')
raw_text = document.raw()
#print( raw_text )

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

input_sentences = sent_tokenize(raw_text )
def get_pos_tags(input_sentences):
    try:
        for sentence in input_sentences:
            print("-------------------------------------------")
            print("[",sentence,"]")
            words = word_tokenize( sentence )
            print (words)
            tagged_words = nltk.pos_tag(words)        
            print(tagged_words)
    except Exception as e:
        print(str(e))

get_pos_tags( input_sentences )

