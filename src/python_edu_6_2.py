#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第6回演習問題1問目
#author: Toki Kawara
#date: 2022/3/18
#######################################

doc = 'i bought an apple .\ni ate it .\nit is delicious .'
word2freq = {}
sents = doc.split('\n')
for sent in sents:
    words = sent.split()
    for word in words:
        word2freq[word] = word2freq.get(word, 0) + 1

print(word2freq)
