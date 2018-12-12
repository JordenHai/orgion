#-*- coding:utf-8 -*-

def foo():
    print('in the foo')
    def bar():
        print("in the bar")

    bar()
# 在函数体内去声明一个函数
# 函数嵌套
