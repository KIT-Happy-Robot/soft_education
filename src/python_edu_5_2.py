#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第5回演習問題2問目
#author: Kazuki Shiba
#date: 2022/3/18
#######################################

li = [1, 2, 3, 4, 5, 6, 7]
for i, j in enumerate(li):
    if i % 2 == 0:
        print(j)