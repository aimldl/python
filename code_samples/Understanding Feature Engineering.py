#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ufe-3-text-preprocessing.py
Understanding Feature Engineering
Understanding Feature Engineering (Part 3)

# Topics
Text Pre-Processing
Bag of Words Model
Bag of N-Grams Model
TF-IDF Model
Document Similarity
Document Clustering with Similarity Features
Topic Models
Document Clustering with Topic Model Features

[Traditional Methods for Text Data
Traditional strategies for taming unstructured, textual data](https://towardsdatascience.com/understanding-feature-engineering-part-3-traditional-methods-for-text-data-f6f7d70acd41)
## Text pre-processing
There can be multiple ways of cleaning and pre-processing textual data. 
In the following points, we highlight some of the most important ones 
  which are used heavily in Natural Language Processing (NLP) pipelines.
  
### Removing tags:
Our text often contains unnecessary content like HTML tags, 
  which do not add much value when analyzing text.
The BeautifulSoup library does an excellent job in providing necessary functions for this.
### Removing accented characters:
In any text corpus, especially if you are dealing with the English language, 
  often you might be dealing with accented characters\letters. 
Hence we need to make sure that these characters are converted 
  and standardized into ASCII characters.
A simple example would be converting é to e.
### Expanding contractions:
In the English language, contractions are basically shortened versions of words or syllables.
These shortened versions of existing words or phrases are created by removing specific letters and sounds. Examples would be, do not to don’t and I would to I’d. Converting each contraction to its expanded, original form often helps with text standardization.
### Removing special characters:
Special characters and symbols which are usually non alphanumeric characters 
  often add to the extra noise in unstructured text.
More than often, simple regular expressions (regexes) can be used to achieve this.
### Stemming and lemmatization:
Word stems are usually the base form of possible words
  that can be created by attaching affixes like prefixes and suffixes
  to the stem to create new words. This is known as inflection.
The reverse process of obtaining the base form of a word is known as stemming.
A simple example are the words WATCHES, WATCHING, and WATCHED.
They have the word root stem WATCH as the base form.
Lemmatization is very similar to stemming,
  where we remove word affixes to get to the base form of a word.
However the base form in this case is known as the root word
  but not the root stem.
  
The difference being that
  the root word is always a lexicographically correct word (present in the dictionary)
  but the root stem may not be so.
### Removing stopwords:
Words which have little or no significance
  especially when constructing meaningful features from text are known as
  stopwords or stop words.
These are usually words that end up having the maximum frequency 
  if you do a simple term or word frequency in a corpus.
Words like a, an, the, and so on are considered to be stopwords.
There is no universal stopword list but we use
  a standard English language stopwords list from nltk.
You can also add your own domain specific stopwords as needed.
"""

#%%
import numpy as np
import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt

pd.options.display.max_colwidth = 200
#%matplotlib inline

#%%####################
# Text Pre-Processing #
#######################
corpus = ['The sky is blue and beautiful.',
          'Love this blue and beautiful sky!',
          'The quick brown fox jumps over the lazy dog.',
          "A king's breakfast has sausages, ham, bacon, eggs, toast and beans",
          'I love green eggs, ham, sausages and bacon!',
          'The brown fox is quick and the blue dog is lazy!',
          'The sky is very blue and the sky is very beautiful today',
          'The dog is lazy but the brown fox is quick!']
labels = ['weather', 'weather', 'animals', 'food', 'food', 'animals', 'weather', 'animals']

corpus = np.array( corpus )
#corpus
#array(['The sky is blue and beautiful.',
#          ...
#       'The dog is lazy but the brown fox is quick!'], dtype='<U66')

corpus_df = pd.DataFrame({'Document': corpus,
                          'Category': labels})
#corpus_df = corpus_df[['Document', 'Category']]  # Why is this necessary?
print( corpus_df )
#                                                             Document Category
#0                                      The sky is blue and beautiful.  weather
#1                                   Love this blue and beautiful sky!  weather
#2                        The quick brown fox jumps over the lazy dog.  animals
#3  A king's breakfast has sausages, ham, bacon, eggs, toast and beans     food
#4                         I love green eggs, ham, sausages and bacon!     food
#5                    The brown fox is quick and the blue dog is lazy!  animals
#6            The sky is very blue and the sky is very beautiful today  weather
#7                         The dog is lazy but the brown fox is quick!  animals

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')
print( type(stop_words) )
# <class 'list'>
#print( stop_words )

def normalize_document( doc ):
    '''
    [^a-zA-Z\s]
    RegExr was created by gskinner.com, and is proudly hosted by Media Temple.
    Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & Javascript flavors of RegEx are supported.
    The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community, and view patterns you create or favorite in My Patterns.
    Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.
    RegExr was created by gskinnercom and is proudly hosted by Media Temple
    Edit the Expression  Text to see matches Roll over matches or the expression for details PCRE  Javascript flavors of RegEx are supported
    The side bar includes a Cheatsheet full Reference and Help You can also Save  Share with the Community and view patterns you create or favorite in My Patterns
    Explore results with the Tools below Replace  List output custom results Details lists capture groups Explain describes your expression in plain English
    
    re.I  ignore case
    re.A  ASCII-only matching
    re.ASCII¶
    Make \w, \W, \b, \B, \d, \D, \s and \S perform ASCII-only matching instead of full Unicode matching.
    This is only meaningful for Unicode patterns, and is ignored for byte patterns. Corresponds to the inline flag (?a).
    Note that for backward compatibility, the re.U flag still exists (as well as its synonym re.UNICODE and its embedded counterpart (?u)), 
    but these are redundant in Python 3 since matches are Unicode by default for strings (and Unicode matching isn’t allowed for bytes).
    '''
    print(doc)
    # remove special characters/whitespaces
    print('remove special characters/whitespaces')
    doc = re.sub(r'[^a-zA-Z\s]','', doc, re.I|re.A)
    print('-'*70)
    print( doc )
    
    # lower case
    print('lower case')
    doc = doc.lower()
    print('-'*70)
    print( doc )
    
    # remove leading and trailing spaces
    print('remove leading and trailing spaces')
    doc = doc.strip()
    print('-'*70)
    print( doc )
    
    # tokenize document
    tokens = wpt.tokenize(doc)
    
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    
    return doc

#normalize_document( corpus_df )
# TypeError: expected string or bytes-like object

normalize_corpus = np.vectorize( normalize_document )
norm_corpus = normalize_corpus( corpus )
print( norm_corpus )
#['sky blue beautiful' 'love blue beautiful sky'
# 'quick brown fox jumps lazy dog'
# 'kings breakfast sausages ham bacon eggs toast beans'
# 'love green eggs ham sausages bacon' 'brown fox quick blue dog lazy'
# 'sky blue sky beautiful today' 'dog lazy brown fox quick']

#%%###################
# Bag of Words Model #
######################
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer( min_df=0, max_df=1.)
cv_matrix = cv.fit_transform( norm_corpus )
cv_matrix = cv_matrix.toarray()
print( cv_matrix )
#[[0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
# [0 0 1 1 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0]
# [0 0 0 0 0 1 1 0 1 0 0 1 0 1 0 1 0 0 0 0]
# [1 1 0 0 1 0 0 1 0 0 1 0 1 0 0 0 1 0 1 0]
# [1 0 0 0 0 0 0 1 0 1 1 0 0 0 1 0 1 0 0 0]
# [0 0 0 1 0 1 1 0 1 0 0 0 0 1 0 1 0 0 0 0]
# [0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 1]
# [0 0 0 0 0 1 1 0 1 0 0 0 0 1 0 1 0 0 0 0]]

# get all unique words in the corpus
vocab = cv.get_feature_names()

# show document feature vectors
cv_matrix_df = pd.DataFrame(cv_matrix, columns=vocab )
print( cv_matrix_df )

#   bacon  beans  beautiful  blue  breakfast  ...  quick  sausages  sky  toast  today
#0      0      0          1     1          0  ...      0         0    1      0      0
#1      0      0          1     1          0  ...      0         0    1      0      0
#2      0      0          0     0          0  ...      1         0    0      0      0
#3      1      1          0     0          1  ...      0         1    0      1      0
#4      1      0          0     0          0  ...      0         1    0      0      0
#5      0      0          0     1          0  ...      1         0    0      0      0
#6      0      0          1     1          0  ...      0         0    2      0      1
#7      0      0          0     0          0  ...      1         0    0      0      0
#
#[8 rows x 20 columns]

#%%#####################
# Bag of N-Grams Model #
########################
# you can set the n-gram range to 1,2 to get unigrams as well as bigrams
bv        = CountVectorizer( ngram_range=(2,2) )
bv_matrix = bv.fit_transform( norm_corpus )

bv_matrix = bv_matrix.toarray()
print( bv_matrix )
#[[0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
# [0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0]
# [1 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 0 1]
# [0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 0 1 0 0 0 0]
# [0 0 0 0 1 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]
# [0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0]
# [0 0 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0]]

vocab     = bv.get_feature_names()
bv_matrix_df = pd.DataFrame( bv_matrix, columns=vocab )
print( bv_matrix_df )
#   bacon eggs  beautiful sky  ...  sky blue  toast beans
#0           0              0  ...         1            0
#1           0              1  ...         0            0
#2           0              0  ...         0            0
#3           1              0  ...         0            1
#4           0              0  ...         0            0
#5           0              0  ...         0            0
#6           0              0  ...         1            0
#7           0              0  ...         0            0
#
#[8 rows x 29 columns]

#%%#############
# TF-IDF Model #
################
# term frequency (tf) and inverse document frequency (idf)
#   tfidf = tf x idf

from sklearn.feature_extraction.text import TfidfVectorizer

tv = TfidfVectorizer( min_df = 0., max_df=1., use_idf=True )
tv_matrix = tv.fit_transform( norm_corpus )
tv_matrix = tv_matrix.toarray()
print( tv_matrix )
#[[0.         0.         0.6009782  0.52692542 0.         0.
#  0.         0.         0.         0.         0.         0.
#  0.         0.         0.         0.         0.         0.6009782
#  0.         0.        ]
# [0.         0.         0.49316188 0.43239428 0.         0.
#  0.         0.         0.         0.         0.         0.
#  0.         0.         0.57150495 0.         0.         0.49316188
#  0.         0.        ]
# [0.         0.         0.         0.         0.         0.38036238
#  0.38036238 0.         0.38036238 0.         0.         0.52594895
#  0.         0.38036238 0.         0.38036238 0.         0.
#  0.         0.        ]
# [0.32116401 0.38321492 0.         0.         0.38321492 0.
#  0.         0.32116401 0.         0.         0.32116401 0.
#  0.38321492 0.         0.         0.         0.32116401 0.
#  0.38321492 0.        ]
# [0.39455357 0.         0.         0.         0.         0.
#  0.         0.39455357 0.         0.47078381 0.39455357 0.
#  0.         0.         0.39455357 0.         0.39455357 0.
#  0.         0.        ]
# [0.         0.         0.         0.3650479  0.         0.41635082
#  0.41635082 0.         0.41635082 0.         0.         0.
#  0.         0.41635082 0.         0.41635082 0.         0.
#  0.         0.        ]
# [0.         0.         0.36082605 0.31636491 0.         0.
#  0.         0.         0.         0.         0.         0.
#  0.         0.         0.         0.         0.         0.72165209
#  0.         0.49893493]
# [0.         0.         0.         0.         0.         0.4472136
#  0.4472136  0.         0.4472136  0.         0.         0.
#  0.         0.4472136  0.         0.4472136  0.         0.
#  0.         0.        ]]
 
vocab = tv.get_feature_names()
tv_matrix_df = pd.DataFrame( np.round(tv_matrix, 2), columns=vocab )
print( tv_matrix_df )
#   bacon  beans  beautiful  blue  ...  sausages   sky  toast  today
#0   0.00   0.00       0.60  0.53  ...      0.00  0.60   0.00    0.0
#1   0.00   0.00       0.49  0.43  ...      0.00  0.49   0.00    0.0
#2   0.00   0.00       0.00  0.00  ...      0.00  0.00   0.00    0.0
#3   0.32   0.38       0.00  0.00  ...      0.32  0.00   0.38    0.0
#4   0.39   0.00       0.00  0.00  ...      0.39  0.00   0.00    0.0
#5   0.00   0.00       0.00  0.37  ...      0.00  0.00   0.00    0.0
#6   0.00   0.00       0.36  0.32  ...      0.00  0.72   0.00    0.5
#7   0.00   0.00       0.00  0.00  ...      0.00  0.00   0.00    0.0
#
#[8 rows x 20 columns]

#%%####################
# Document Similarity #
#######################
# Document similarity is the process of using a distance or similarity based metric 
#   that can be used to identify how similar a text document is with any other document(s) 
#   based on features extracted from the documents like bag of words or tf-idf.
# There are several similarity and distance metrics that are used to compute document similarity. 
# These include cosine distance/similarity, euclidean distance, 
#   manhattan distance, BM25 similarity, jaccard distance and so on.
# In our analysis, we will be using perhaps the most popular and widely used similarity metric,
#   cosine similarity and compare pairwise document similarity based on their TF-IDF feature vectors.

from sklearn.metrics.pairwise import cosine_similarity

similarity_matrix = cosine_similarity( tv_matrix )
similarity_df     = pd.DataFrame( similarity_matrix )
print( similarity_df )
#          0         1         2  ...         5         6         7
#0  1.000000  0.820599  0.000000  ...  0.192353  0.817246  0.000000
#1  0.820599  1.000000  0.000000  ...  0.157845  0.670631  0.000000
#2  0.000000  0.000000  1.000000  ...  0.791821  0.000000  0.850516
#3  0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000
#4  0.000000  0.225489  0.000000  ...  0.000000  0.000000  0.000000
#5  0.192353  0.157845  0.791821  ...  1.000000  0.115488  0.930989
#6  0.817246  0.670631  0.000000  ...  0.115488  1.000000  0.000000
#7  0.000000  0.000000  0.850516  ...  0.930989  0.000000  1.000000
#
#[8 rows x 8 columns]

# documents (0, 1 and 6), (2, 5 and 7) are very similar to one another
#   and documents 3 and 4 are slightly similar to each other but the magnitude is not very strong, 
#   however still stronger than the other documents.

# Cosine similarity basically gives us a metric representing 
#   the cosine of the angle between the feature vector representations 
#   of two text documents.
# Lower the angle between the documents, the closer and more similar they are 
#   as depicted in the following figure.

#%%#############################################
# Document Clustering with Similarity Features #
################################################
# Later

#%%#############
# Topic Models #
################
# Later

#%%##############################################
# Document Clustering with Topic Model Features #
################################################
# Later

#%%##########################################
# Text Pre-Processing: Intermediate Results #
#############################################
# The print output in def normalize_document( doc ).

#The sky is blue and beautiful.
#remove special characters/whitespaces
#----------------------------------------------------------------------
#The sky is blue and beautiful
#lower case
#----------------------------------------------------------------------
#the sky is blue and beautiful
#remove leading and trailing spaces
#----------------------------------------------------------------------
#the sky is blue and beautiful
#The sky is blue and beautiful.
#remove special characters/whitespaces
#----------------------------------------------------------------------
#The sky is blue and beautiful
#lower case
#----------------------------------------------------------------------
#the sky is blue and beautiful
#remove leading and trailing spaces
#----------------------------------------------------------------------
#the sky is blue and beautiful
#Love this blue and beautiful sky!
#remove special characters/whitespaces
#----------------------------------------------------------------------
#Love this blue and beautiful sky
#lower case
#----------------------------------------------------------------------
#love this blue and beautiful sky
#remove leading and trailing spaces
#----------------------------------------------------------------------
#love this blue and beautiful sky
#The quick brown fox jumps over the lazy dog.
#remove special characters/whitespaces
#----------------------------------------------------------------------
#The quick brown fox jumps over the lazy dog
#lower case
#----------------------------------------------------------------------
#the quick brown fox jumps over the lazy dog
#remove leading and trailing spaces
#----------------------------------------------------------------------
#the quick brown fox jumps over the lazy dog
#A king's breakfast has sausages, ham, bacon, eggs, toast and beans
#remove special characters/whitespaces
#----------------------------------------------------------------------
#A kings breakfast has sausages ham bacon eggs toast and beans
#lower case
#----------------------------------------------------------------------
#a kings breakfast has sausages ham bacon eggs toast and beans
#remove leading and trailing spaces
#----------------------------------------------------------------------
#a kings breakfast has sausages ham bacon eggs toast and beans
#I love green eggs, ham, sausages and bacon!
#remove special characters/whitespaces
#----------------------------------------------------------------------
#I love green eggs ham sausages and bacon
#lower case
#----------------------------------------------------------------------
#i love green eggs ham sausages and bacon
#remove leading and trailing spaces
#----------------------------------------------------------------------
#i love green eggs ham sausages and bacon
#The brown fox is quick and the blue dog is lazy!
#remove special characters/whitespaces
#----------------------------------------------------------------------
#The brown fox is quick and the blue dog is lazy
#lower case
#----------------------------------------------------------------------
#the brown fox is quick and the blue dog is lazy
#remove leading and trailing spaces
#----------------------------------------------------------------------
#the brown fox is quick and the blue dog is lazy
#The sky is very blue and the sky is very beautiful today
#remove special characters/whitespaces
#----------------------------------------------------------------------
#The sky is very blue and the sky is very beautiful today
#lower case
#----------------------------------------------------------------------
#the sky is very blue and the sky is very beautiful today
#remove leading and trailing spaces
#----------------------------------------------------------------------
#the sky is very blue and the sky is very beautiful today
#The dog is lazy but the brown fox is quick!
#remove special characters/whitespaces
#----------------------------------------------------------------------
#The dog is lazy but the brown fox is quick
#lower case
#----------------------------------------------------------------------
#the dog is lazy but the brown fox is quick
#remove leading and trailing spaces
#----------------------------------------------------------------------
#the dog is lazy but the brown fox is quick

#The above output should give you a clear view of 
#  how each of our sample documents look like after pre-processing.
# 
#Output
#------
#array(['sky blue beautiful', 'love blue beautiful sky',
#       'quick brown fox jumps lazy dog',
#       'kings breakfast sausages ham bacon eggs toast beans',
#       'love green eggs ham sausages bacon',
#       'brown fox quick blue dog lazy', 
#       'sky blue sky beautiful today',
#       'dog lazy brown fox quick'],
#      dtype='<U51')
