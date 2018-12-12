# -*- coding:utf-8 -*-
# Author: Jorden Hai
import copy

person = ['name',['Saving',100]]

#第二个列表只是第一个列表的引用
#浅copy
'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
'''

p1 = person[:]
p2 = person[:]

p1[0] = 'Alex'
p2[0] = 'FengJie'

p1[1][1] = 50

print(p1)
print(p2)
