#! /usr/bin/python3
# -*- coding: utf-8 -*-
'''
mecab_basic_usage.py
* Draft: 2019-12-10(Tue)

src: mecab-python3 0.996.2
     https://pypi.org/project/mecab-python3/

$ python mecab_basic_usage.py
python	python	python	名詞-固有名詞-組織
が	ガ	が	助詞-格助詞-一般
大好き	ダイスキ	大好き	名詞-形容動詞語幹
です	デス	です	助動詞	特殊・デス	基本形
EOS

$
'''

import MeCab

wakati = MeCab.Tagger("-Owakati")
wakati.parse("pythonが大好きです").split()
#['python', 'が', '大好き', 'です']

chasen = MeCab.Tagger("-Ochasen")
print(chasen.parse("pythonが大好きです"))

