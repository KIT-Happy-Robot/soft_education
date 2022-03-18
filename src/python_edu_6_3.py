#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第6回演習問題1問目
#author: Toki Kawara
#date: 2022/3/18
#######################################

n = input('金額を入力してください:')
n = int(n)
a = n // 100
b = (n - 100 * a) //10
c = (n - 100 * a - 10 * b) // 1
ans = {}
if a != 0:
    ans['100円玉'] = a
if b != 0:
    ans['10円玉'] = b
if c != 0:
    ans['1円玉'] = c

print(ans)
