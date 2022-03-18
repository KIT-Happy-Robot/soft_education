#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第5回演習問題1問目
#author: Kazuki Shiba
#date: 2022/3/18
#######################################

xs = [1, 1, 1, 3, 3, 5, 2, 2, 3]
ys = []
for i in range(len(xs)):
    if i == 0:
        ys.append(xs[i])
    elif xs[i] != xs[i - 1]:
        ys.append(xs[i])
print(ys)