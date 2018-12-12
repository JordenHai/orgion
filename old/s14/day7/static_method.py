# -*- coding:utf-8 -*-
# Author: Jorden Hai
import os




class Dog(object):

    n = 0

    def __init__(self,name):

        self.name = name
        self.__food = None


    def __call__(self, *args, **kwargs):
        print("---->",args,kwargs)

    def __str__(self):#打印类的时候返回什么 由这个地方定义
        return "<obj:%s>"%(self.name)
    #相当于一个单纯的函数 只是一个函数
    #必须要通过类名调用
    #高级语法 在一些特定场景中
    # @classmethod #只能调用类属性
    # @staticmethod#实际上跟类什么关系了
    @property #方法变成静态属性
    def eat(self):
        print("%s is eatting %s"%(self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print("%s is eatting %s" % (self.name, food))
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print('删完了')


d = Dog("chengzhonghua")
d.eat
d.eat = 'food'
d.eat
d(11,22,33,name = 3)
del d.eat
print(d.__dict__)
print(Dog.__dict__)
print(d)
print(d)

