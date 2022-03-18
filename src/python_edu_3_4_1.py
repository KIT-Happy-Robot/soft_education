#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第3,4回演習問題1問目
#author: Kazuki Shiba
#date: 2022/3/18
#######################################

start = int(input('start: '))
stop = int(input('stop: '))
for i in range(start, stop + 1):
    if i % 3 == 0:
        if i % 5 == 0:
            ans = 'FizzBuzz'
        else:
            ans = 'Fizz'
    else:
        if i % 5 == 0:
            ans = 'Buzz'
        else:
            ans = str(i)
    print(ans)