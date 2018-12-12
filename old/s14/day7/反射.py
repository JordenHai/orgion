# -*- coding:utf-8 -*-
# Author: Jorden Hai

def bulk(self):
    print("%s is yelling..."%(self.name))

class Dog(object):

    def __init__(self,name):
        self.name = name


    def eat(self,food):
        print("%s is eating ..."%self.name,food)


d = Dog('ChenZhonghua')
L = ['name']
choice = input("-->:".strip())

if hasattr(d,choice):
    getattr(d,choice)
else:
    setattr(d,choice,bulk)
    v = getattr(d,choice)
    v(d)

'''
if hasattr(d,choice):
    if choice not in L:
        func = getattr(d,choice)#得到地址
        food = input("food-->")
        func(food)
    else:
        attr = getattr(d,choice)
        name = input("Name-->")
        setattr(d,choice,name)
        print(getattr(d,choice))
else:
    # setattr(d,choice,bulk)#d.choice = bulk
    # d.talk(d)
    setattr(d,choice,22)#d.choice = 22
    print(getattr(d,choice))
'''
'''
if choice == 'eat':
    d.eat()
'''