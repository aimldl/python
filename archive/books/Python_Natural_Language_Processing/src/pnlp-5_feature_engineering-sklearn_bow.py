# -*- coding: utf-8 -*-
"""
pnlp-5_feature_engineering-sklearn_bow.py

Source: Python Natural Language Processing
Advanced machine learning and deep learning techniques for natural language processing
Jalaj Thanaki

파이썬 자연어 처리의 이론과 실제
효율적인 자연어 처리를 위한 머신 러닝과 딥러닝 구현하기
05. 피러 엔지니어링과 NLP 알고리즘 > NLP의 기본 피쳐 > BoW (Bag-of-Words)
pp.196~198

"""

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

ngram_vectorizer = CountVectorizer( analyzer='char_wb', ngram_range=(2,2), min_df=1 )
# List is number of documents here.
# Two documents and each has only one word.

counts = ngram_vectorizer.fit_transform( ['words','wprds'] )
ngram_vectorizer.get_feature_names() == ( ['w', 'ds', 'or', 'pr', 'rd' , 's','wo','wp'] )
print( counts.toarray().astype(int) )
#[[1 1 1 0 1 1 1 0]
# [1 1 0 1 1 1 0 1]]
