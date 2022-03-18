#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第5回演習問題1問目
#author: Kazuki Shiba
#date: 2022/3/18
#######################################

li1 = list(range(1, 32))
li2 = list(range(1, 13))
count = 0
for i in li1:
    for j in li2:
        if i % 10 == j % 10:
            count += 1
print(count)