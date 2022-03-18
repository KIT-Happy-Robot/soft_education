#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第3,4回演習問題2問目
#author: Kazuki Shiba
#date: 2022/3/18
#######################################

count = 1
print('カレーを召し上がれ')
while 1:
    print(str(count) + '皿のカレーを食べました')
    key = input('おかわりはいかがですか？（y/n）: ')
    if key == 'y':
        count += 1
    else:
        break
print('ごちそうさまでした')