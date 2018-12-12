#-*- coding:utf-8 -*-

m = 5
l = [i*2 for i in range(m)]
#列表生成式
c = (i*2 for i in range(1000000))


# 生成器 只有在调用的时候才会生成相应的数据
# 你调用那一次 才会产生那一次的数据

def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])

s = dec2bin(25)
