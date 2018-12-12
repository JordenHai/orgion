#-*- coding:utf-8 -*-
import time

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)  #运行 传入的函数
        stop_time = time.time()
        print("the func run time:%.5s" % (stop_time - start_time))
    return deco

@timer
def test1():
    time.sleep(2)
    print("in the test1")

@timer  #test2 = timer(test2) =deco test2(name) = deco(name)
def test2(name):
    print("test2:",name)

test1()
test2("alex")


