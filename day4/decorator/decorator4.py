#-*- coding:utf-8 -*-
import time


def test1():
    time.sleep(2)
    print("in the test1")


def test2():
    time.sleep(2)
    print("in the test2")

def dec_time(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time:%s"%(stop_time-start_time))
    return func

test1 = dec_time(test1)
test1()
test2 = dec_time(test2)
test2()

