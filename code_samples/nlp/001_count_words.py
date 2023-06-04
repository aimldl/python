#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO: Delete this line. 코드에 적용완료 2019-08-8 (목)

import re
from collections import Counter

def count_words(text):
    # Count how many times each unique word occurs in text.
    print("count_words")    
    # print(text)
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    print(counts)
    
    # TODO: Convert to lowercase
    text_lower = text.lower()
    print( text_lower)

    # TODO: Split text into tokens (words), leaving out punctuation
    # (Hint: Use regex to split on non-alphanumeric characters)
    tokens = re.split('[^a-zA-Z]',text_lower)
    print(tokens)
    
    # TODO: Aggregate word counts using a dictionary
    counts = Counter(tokens)    
    print("-")
    print(counts)
    
    return counts


def test_run():
    with open("count_words-input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
    
'''
udacity_nlp_python
'''
