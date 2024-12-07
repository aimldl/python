# test_pos_tagging.py

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

def get_pos_tags(input_sentences):
    try:
        for sentence in input_sentences:
            words = nltk.word_tokenize( sentence )
            tagged_words = nltk.pos_tag(words)
            print(tagged_words)
    except Exception as e:
        print(str(e))
        
get_pos_tags( sentence_tokenized_test_text )

