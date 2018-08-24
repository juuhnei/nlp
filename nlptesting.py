# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Testing nltk and open nlp syntax
import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg


alice = gutenberg.raw(fileids = 'carroll-alice.txt')
print (len(alice))