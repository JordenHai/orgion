# -*- coding:utf-8 -*-
# Author: Jorden Hai

class Dog():
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s :Wang Wang Wang"%self.name)


d1 = Dog("陈中华")
d2 = Dog("杨哲")
d3 = Dog("焦海")

d1.bulk()
d2.bulk()
d3.bulk()
