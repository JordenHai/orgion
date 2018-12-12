# -*- coding:utf-8 -*-
# Author: Jorden Hai

class Foo(object):#来自于python

    def __init__(self,name):
        self.name = name

def func(self):
    print("Hello Jorden")



def __init__(self,name,age):
    self.name = name
    self.age = age


obj = Foo("ALEX")

jh = type('jh',(object,),{'func':func,
                          '__init__':__init__})





