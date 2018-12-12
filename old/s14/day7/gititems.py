# -*- coding:utf-8 -*-
# Author: Jorden Hai

class Foo(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print("__getitems__",key,self.data[key])
    def __setitem__(self, key, value):
        print("__setutem__",key,value)
        self.data[key] = value

    def __delitem__(self, key):
        print("__delitem__",key)

obj = Foo()

obj['name'] = 'Alex'


print(obj['name'])

print(obj.data)