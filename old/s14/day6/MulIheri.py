# -*- coding:utf-8 -*-
# Author: Jorden Hai

class A():

    def __init__(self):
        print("init in A")

class B(A):

    def __init__(self):
        A.__init__(self)
        print("init in B")
class C(A):

    def __init__(self):
        A.__init__(self)
        print("init in C")

class D(B,A): #找到第一个就停下来
    pass
#
#               A
#             |   \
#           B       C
#               D
#继承策略

#继承方向 从D --> B --> C --> A  广度优先查找
#
#从python3中经典类新式类按照广度优先
#从python2中经典类中深度优先来继承 新式类按照广度优先来继承
#
#继承方向 从D --> B --> A --> C  深度优先查找



a = D()