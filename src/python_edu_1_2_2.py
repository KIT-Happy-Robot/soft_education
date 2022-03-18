#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第1,2回演習問題2問目
#author: Kazuki Shiba
#date: 2022/3/18
#######################################

jap = int(input('国語のテストの点数を入力してください: '))
mat = int(input('数学のテストの点数を入力してください: '))
sci = int(input('理科のテストの点数を入力してください: '))
his = int(input('社会のテストの点数を入力してください: '))
eng = int(input('英語のテストの点数を入力してください: '))
ave = (jap + mat + sci + his + eng) / 5
print('5科目の平均点は' + str(ave) + '点です')