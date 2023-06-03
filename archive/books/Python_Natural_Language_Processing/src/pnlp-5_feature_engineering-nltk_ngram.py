# -*- coding: utf-8 -*-
"""
pnlp-5_feature_engineering-nltk_ngram.py

Source: Python Natural Language Processing
Advanced machine learning and deep learning techniques for natural language processing
Jalaj Thanaki

파이썬 자연어 처리의 이론과 실제
효율적인 자연어 처리를 위한 머신 러닝과 딥러닝 구현하기
05. 피러 엔지니어링과 NLP 알고리즘 > NLP의 기본 피쳐 > n그램
pp.193~195

"""

from nltk import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 4
sentence_split = sentence.split()
print( sentence_split )
#['this', 'is', 'a', 'foo', 'bar', 'sentences', 'and', 'i', 'want', 'to', 'ngramize', 'it']

ngramsres = ngrams( sentence_split, n)
for grams in ngramsres:
    print( grams )
#    ('this', 'is', 'a', 'foo')
#    ('is', 'a', 'foo', 'bar')
#    ('a', 'foo', 'bar', 'sentences')
#    ('foo', 'bar', 'sentences', 'and')
#    ('bar', 'sentences', 'and', 'i')
#    ('sentences', 'and', 'i', 'want')
#    ('and', 'i', 'want', 'to')
#    ('i', 'want', 'to', 'ngramize')
#    ('want', 'to', 'ngramize', 'it')
