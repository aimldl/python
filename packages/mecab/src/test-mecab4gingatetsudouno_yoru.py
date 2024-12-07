#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
packages/mecab/src/test-mecab4gingatetsudouno_yoru.py

* Draft: 2019-12-18(Wed)
* Base code: packages/mecab/src/mecab_basic_usage.py

* Prerequisite
  * Install Python Package MeCab

* Usage:
$ python test-mecab4gingatetsudouno_yoru.py
python	python	python	名詞-固有名詞-組織
が	ガ	が	助詞-格助詞-一般
大好き	ダイスキ	大好き	名詞-形容動詞語幹
です	デス	です	助動詞	特殊・デス	基本形
EOS

$
'''

import MeCab

wakati = MeCab.Tagger("-Owakati")
chasen = MeCab.Tagger("-Ochasen")

file = "../text_files/clean_gingatetsudouno_yoru.txt"
with open( file, 'r' ) as f:
    for line in f:
        line.rstrip()  # Remove the last character or \n.
        wakati.parse( line ).split()
        #print(chasen.parse( line ))
        analyzed_line = chasen.parse( line )
        print( analyzed_line )

