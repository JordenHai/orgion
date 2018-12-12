#-*- coding:utf-8 -*-
import math
import time
def bar():
    time.sleep(0.21)
    print("in the bar")

def test(func):
    start_time  = time.time()
    func()
    stop_time = time.time()
    print("the function run time is %s"%(stop_time-start_time))
#可以运行
#加上括号就可以运行
#func只是个门牌号 他们都指向同一个内存地址

test(bar)

