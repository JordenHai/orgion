# -*- coding:utf-8 -*-
# Author: Jorden Hai
class MyType(type):
    def __init__(self,what,bases=None,dict=None):
        print("--MyType init--")
        super(MyType,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call--")
        obj = self.__new__(self,*args,**kwargs)#开辟了内存空间
        self.__init__(obj,*args,**kwargs)

    #call 来创建new
    #new来执行init

class Foo(object):

    __metaclass = MyType
    def __init__(self,name):
        self.name = name
        print("Foo --INIT--")
    def __new__(cls, *args, **kwargs):
        print("FOO --NEW--")
        return object.__new__(cls)#继承父亲的__new__方法

f = Foo("jj")
f.name