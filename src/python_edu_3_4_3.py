#!/usr/bin/env python
#-*- coding: utf-8 -*-

#######################################
#title: python講習会第3,4回演習問題3問目
#author: Kazuki Shiba
#date: 2022/3/18
#######################################

hp = 300
while hp > 0:
    dmg = int(input('与えるダメージ数を100以下の整数で入力してください: '))
    if dmg > 100:
        print('ミス！ダメージを与えられない！')
    else:
        print('魔王Okuseに' + str(dmg) + 'のダメージ！')
        hp -= dmg
print('魔王Okuseを倒した！')