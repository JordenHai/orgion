#-*- coding:utf-8 -*-
import time

def bar():
    time.sleep(0.2)
    print("in the bar")
    pass

def test2(func):
    print(func)
    return func

bar = test2(bar)
bar()
print(bar)