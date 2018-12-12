#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import random
round_num = 8
n = 20
a = -1
b = 1


def init_array():
    list_x = []
    list_y = []
    for i in range(n+1):
        num = a + (b-a)/n*i
        num = round(num,round_num)
        list_x.append(num)

    for i in range(n+1):
        num = 1/(1 + 25*list_x[i]*list_x[i])
        num = round(num,round_num)
        list_y.append(num)
    return list_x,list_y
    pass

def W_new_1(num,num_t):
    ploy_sum = 1
    for i in range(n+1):
        if i == num_t:
            continue
        else:

            ploy_sum = np.poly1d([0,1,-num[i]]) * ploy_sum
    return ploy_sum

def W_new(num,num_t):
    ploy_sum = 1
    for i in range(n+1):
        if i == num_t:
            continue
        else:
            ploy_sum = round(ploy_sum * (num[num_t]-num[i]),round_num)
    return ploy_sum

def ln_sum(list_x,list_y):
    sum_ln = []
    for i in range(n+1):
        W_new_x = W_new(list_x,i)
        W_new_y = W_new_1(list_x,i)
        W_new_x = round(list_y[i]/W_new_x,round_num)
        W_new_y = W_new_x*W_new_y
        sum_ln.append(W_new_y)
    return sum_ln


x,y = init_array()
T = np.array(x)
ln = sum(ln_sum(x,y))
ln_y = ln(x)
power = np.array(ln_y)
x_new = np.linspace(T.min()，T.max(),300)

power_smooth = spline(T,power,x_new)

