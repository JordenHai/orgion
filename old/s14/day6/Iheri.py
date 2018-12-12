# -*- coding:utf-8 -*-
# Author: Jorden Hai

class People(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eatting "%self.name)

    def sleep(self):
        print("%s is sleepping "%self.name)

    def talk(self):
        print("%s is talking " % self.name)

class Man(People):

    def __init__(self,name,age,money):
        People.__init__(self,name,age)
        self.money = money

    def piao(self):
        print("%s........."%self.name)

    def sleep(self):#chongxie
        People.sleep(self)
        print("Man is sleepping ")

    def debt(self):
        print("%s is debting"%self.name)

class Woman(People):
    def get_baby(self):
        print("%s is born a baby"%self.name)

m1 = Man('yz',15,15)
m1.eat()
m1.sleep()


w1 = Woman("czh",26)

w1.get_baby()
