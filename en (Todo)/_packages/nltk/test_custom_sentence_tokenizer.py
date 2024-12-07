# test_custom_sentence_tokenizer.py

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

training_text = state_union.raw("2005-GWBush.txt")
test_text = state_union.raw("2006-GWBush.txt")

#print(training_text)
#print(test_text)
custom_sentence_tokenizer = PunktSentenceTokenizer(training_text)
sentence_tokenized_test_text = custom_sentence_tokenizer.tokenize(test_text)

#print(sentence_tokenized_test_text)

def print_sentence_tokenized_text(input_sentences):
    try:
        for sentence in input_sentences:
            print("[",sentence,"]")
    except Exception as e:
        print(str(e))
        
print_sentence_tokenized_text( sentence_tokenized_test_text )

