# -*- coding: utf-8 -*-
"""
newspaper_url2txt.py

Package Newspaper3k

Reference
- Newspaper On Python, DANIEL HOADLEY, JANUARY 5, 2017
  http://carrefax.com/new-blog/2017/1/5/newspaper-on-python

import Newspaper

"""
from newspaper import Article
import sys

# Configure
script_name = sys.argv[0]
argc = len( sys.argv )
arguments = str( sys.argv )
#print(script_name, argc, arguments)

# Assume a single argument
url = arguments
url = 'https://news.v.daum.net/v/20181107151357298'
language='ko'
print('lang=',language, 'url=',url)

# Prerequisite:
# from newspaper import Article  # pip install newspaper3k
# "get_news_article" gets a newspaper article from an url

def get_news_article( url, lang='ko' ):
    doc_ = Article( url, language=lang )
    doc_.download()
    doc_.parse()
    print( doc_.title )
    filename_ = doc_.title[:30] + '.txt'
    #print( doc.txt[:50] )
    return doc_, filename_

def url2txt( url, lang='ko' ):
    doc, filename = get_news_article( url, lang )
    # Write the body of the document to a file
    print("Saving the URL to", filename, "...")
    f = open( filename,'w' )
    f.write( doc.text )
    
url2txt( url,language )
