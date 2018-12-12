#-*- coding:utf-8 -*-
import time
# 协层
def consumer(name):
    print("%s ready to eat baozi"%name)
    while True:
        baozi = yield#保存当前状态 返回 调用send会唤醒然后传递值
        # next 只是在唤醒
        print("baozi[%s]coming,eated by [%s]"%(baozi,name))
    pass

def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')
    # 只是将其变化生成器
    c1.__next__()
    c2.__next__()
    # 消费者生成之后 第一个next指挥执行到 yield
    # send 会将值传递到yield 然后顺序执行
    # next 不会传递值 只是执行
    print("老子开始准备做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子")
        c1.send(i)
        c2.send(i)
    pass
# 异步 IO
# 底层
# 协层
producer('12')