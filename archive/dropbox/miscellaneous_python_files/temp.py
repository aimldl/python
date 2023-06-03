# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 22:43:43 2019

@author: aimldl
"""

"""
    #%%
    def tokenize_sentences(self, df):
        '''
        Sentence tokenization is required to properly perform word tokenization.
        However there are so many sentences in casual language that it's
        difficult to tokenize by sentences. There're some hints to indicate
        the end of a sentence such as \n, \c, and 
        I wonder if there's any meaning to
        '''
        assert isinstance(df, pd.DataFrame), 'df must be a dataframe.'
        
        return df
    
    def tokenize_words(self, df):
        '''
        This is a custom word tokenizer like NLTK's RegexpTokinizer with
        regular expression \w+\$[\d\.]+|\S+
        '''
        assert isinstance(df, pd.DataFrame), 'df must be a dataframe.'
        
        p = regex.compile( '\w+\$[\d\.]+|\S+' )
        # TODO: ***
#        df['token'] = df['review'].apply( lambda x: p.match(x).group() )
        
        return df
    
    def remove_stopwords(self, df):
        '''
        Casual language is included:
            Hi, Hey, Hello, How are u?
        Doesn't affect the sentiment analysis result.
        '''
        assert isinstance(df, pd.DataFrame), 'df must be a dataframe.'
        
        #p.120 Python NLP book
                
        return df

    def encode(self, df):
        '''
        df['sentiment'] = encode( df['sentiment'], 'sentiment')
        series = [1 if sentiment == 'positive' else 0 
                 for sentiment in series.values]
        '''
        for sentiment in df['sentiment']:
            if sentiment == 'Positive':
                
            elif sentiment == 'Neutral':
            elif sentiment == 'Negative':

#    def lexical_diversity( self, text ):
#        '''
#        Lexical diversity = number of tokens / number of vocaburary
#        
#        Note text should be properly normalized and cleansed 
#        to get accurate lexical diversity. When raw text is given,
#        you can have a rough idea about text.
#        '''
#        num_of_tokens     = len( text )
#        num_of_vocaburary = len( set(text) )
#        lexical_diversity = num_of_tokens / num_of_vocaburary
#        
#        return lexical_diversity

                
# This is from one of earlier .ipynb file.
# Delete this if not used. I keep this just in case.
#        # type(sentence) is <class 'str'>
#    for sentence in df[ 'roman_urdu' ]:
#        normalized_sentence = sentence.lower()
#        #words = normalized_sentence.split()
#        #print( normalized_sentence )
#        normalized_and_split_sentence = normalized_sentence.split(" ")
#        print(normalized_and_split_sentence)
    # TODO: DOuble check this
    
    # TODO: DOuble check this
    def percentage(self, count, total):
        '''
        Usage:
          percentage( text.count('myword'), len(text))
        '''
        return 100*count/total
    
    def encode(self, df):
        '''
        df['sentiment'] = encode( df['sentiment'], 'sentiment')
        series = [1 if sentiment == 'positive' else 0 
                 for sentiment in series.values]
        '''
#        for sentiment in df['sentiment']:
#            if sentiment == 'Positive':
#                
#            elif sentiment == 'Neutral':
#            elif sentiment == 'Negative':

    #%%
    def convert_characters(self, df):
        '''
        Broken characters are converted to alphabets.
        
        U+C000?ì U+CFFF ?ì ? ëì½ë ë¬¸ì ëª©ë¡
        https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C_C000~CFFF
        
        ?????Î¿??
        ????
         ???????????????
         ?ë­?ë«??????Î¿????I m lucky ?????
         ?????????
         
         
         
        '''
        '''
        https://pypi.org/project/regex/
        Unicode
        This module supports Unicode 12.1.0.
        
        Full Unicode case-folding is supported.
        
        Additional features
        The issue numbers relate to the Python bug tracker, except where listed as ?Hg issue??
        
        Added support for lookaround in conditional pattern (Hg issue 163)
        
        The test of a conditional pattern can now be a lookaround.
        
        Examples:
        
        >>> regex.match(r'(?(?=\d)\d+|\w+)', '123abc')
        <regex.Match object; span=(0, 3), match='123'>
        >>> regex.match(r'(?(?=\d)\d+|\w+)', 'abc123')
        <regex.Match object; span=(0, 6), match='abc123'>
        This is not quite the same as putting a lookaround in the first branch of a pair of alternatives.
        
        Examples:
        
        >>> print(regex.match(r'(?:(?=\d)\d+\b|\w+)', '123abc'))
        <regex.Match object; span=(0, 6), match='123abc'>
        >>> print(regex.match(r'(?(?=\d)\d+\b|\w+)', '123abc'))
        None
        In the first example, the lookaround matched, but the remainder of the first branch failed to match, and so the second branch was attempted, whereas in the second example, the lookaround matched, and the first branch failed to match, but the second branch was not attempted.
        '''
        assert isinstance(df, pd.DataFrame), 'df must be a dataframe.'
        
        return df
"""
     
"""
# Overview
This task is done in the order of:
  1. Text Preprocessing
  2. 텍스트 구문 분석(parsing) 및 탐색 데이터 분석
  3. Feature Extraction
  4. Training a Deep Learning Model
  5. Evaluation 
Deployment is, typically, the last step which is skipped in this task.

# 
## 1. Text Preprocessing

## 2. Text Parsing & etc

## 3. Feature Extraction (FE)
FE is a step to present the text into 

vector space representation.
Simply said, convert text to numeric vectors.
Each dimension of the vector is a specific feature/attribute.

Bag of Word (BoW) model
Each dimension is a specific word "from the corpus".

The value could be occurence (0 or 1), frequency, or weighted values.
Each document is represented as a 'bag' of its own words.

The drawback of this model is the word orders, sequence, and grammaer are ignored.

Bag of N-Grams Model
If a unigram or 1-gram (N=1) is used, this is same as the BoW model.
If bi-gram/2-gram (N=2) or tri-gram/3-gram (N=3) is used, a phrase or collection
of words can be taken into account.

TF-IDF (Term Frequency-Inverse Document Frequency)
In a large corpus, the above methods can't be used 
because some terms occur frequently across all documents and they tend to
overshadow other terms in the feature set. To tackle this problem, these terms
can be "normalized" by document frequency.

TF x IDF
itidf(w,D) = tf(w,D) x idf(w,D) = tf(w,D) x log(C/df(w))

idf(w,D) = log(C/df(w))
where C is the total number of documents in the corpus C and
      df(w) document frequency of the word w,
        which is basically the frequency of documents in the corpus where the word w occurs.
So
df(w)/C means the document frequency of word w divided by the total number of documents.
The ratio of word w in the corpus C in terms of document.

Then why is this value inversed? Many df(w) are too small with respect to C.
So the number will be technically 0 considering the floating numbers a computer can express.
TF x IDF = TF x 0 = 0.
So it's hard to express the differences.
C/df(w) will result in a very large number. Technically, infinity.
To scale down this number, logarithm can be taken!

Interested readers who might want to dive into further details of how the internals of this model work can refer to page 181 of Text Analytics with Python (Springer\Apress; Dipanjan Sarkar, 2016).

After converting a document into a vector, I can pick some samples to see the similarity between documents.
Even though I don't understand Urdu, I can select some obviously similar documents and compute the distance.
For the distance metric, I may use the popular 'cosine similatiry' among cosine, Euclidean, manhattan, BM25, jaccard distance and so on.
The lower the angle between documents, the closer or more similar they are.

The small table shows the document similarity which gives a certain degree of
measure for judgement. Of course, I can use Google Translate to understand the selected
'clean' sentences.

a document-term matrix

## 4. Training a Deep Learning Model

## 5. Evaluation
"""