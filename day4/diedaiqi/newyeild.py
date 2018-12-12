#-*- coding:utf-8 -*-
def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            while l.__len__() < 5:
                l.append(str(0))
            return ''.join(l[::-1])
