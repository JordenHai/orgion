#-*- coding:utf-8 -*-

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a,b = b,a+b
        #上面这个操作是
        # t = (b,a+b)
        # a = t[0]
        # b = t[1]
        n = n+1
    return 'done'
    #异常时候打印的消息
    #
# 这个不是递归
# 这个只是函数操作
f = fib(10)
while True:
    try:
        x = next(f)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break