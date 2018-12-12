#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
round_num = 9
a = -1
b = 1

chart_x_y = {}

def plt_show(str):
    plt.title('line chart '+str)
    plt.xlabel('x')
    plt.ylabel('y')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')  # 设置 上、右 两条边框不显示
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')  # 将下、左 两条边框分别设置为 x y 轴
    plt.legend(loc = 'best')
    plt.show()
    pass

def init_array(n):
    list_x = []
    list_y = []
    for i in range(n + 1):
        num = a + (b - a) / n * i
        num = round(num, round_num)
        list_x.append(num)

    for i in range(n + 1):
        num = 1 / (1 + 25 * list_x[i] * list_x[i])
        num = round(num, round_num)
        list_y.append(num)
    return list_x, list_y
    pass


def W_new_1(num, num_t):
    ploy_sum = 1
    n = len(num) -1
    for i in range(n + 1):
        if i == num_t:
            continue
        else:

            ploy_sum = np.poly1d([0, 1, -num[i]]) * ploy_sum
    return ploy_sum


def W_new(num,num_t):
    ploy_sum = 1
    n = len(num) -1
    for i in range(n + 1):
        if i == num_t:
            continue
        else:
            ploy_sum = round(ploy_sum * (num[num_t] - num[i]), round_num)
    return ploy_sum


def ln_sum(list_x, list_y):
    sum_ln = []
    n = len(list_x) -1
    for i in range(n + 1):
        W_new_x = W_new(list_x, i)
        W_new_y = W_new_1(list_x, i)
        W_new_x = round(list_y[i] / W_new_x, round_num)
        W_new_y = W_new_x * W_new_y
        sum_ln.append(W_new_y)
    return sum_ln

def plt_show():
    plt.title('line chart')
    plt.xlabel('x')
    plt.ylabel('y')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')  # 设置 上、右 两条边框不显示
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')  # 将下、左 两条边框分别设置为 x y 轴
    plt.legend(loc = 'best')
    plt.show()
    pass

L = [5,10,15]
# for i in L:
#     x, y = init_array(i)
#     n = len(x) - 1
#     ln = sum(ln_sum(x, y))
#     ln_y = ln(x)
#     T = np.array(x)
#     if n == 5:
#         power = np.array(ln_y)
#         x_new = np.linspace(T.min(), T.max(),500)
#         power_smooth = spline(T, power, x_new)
#         plt.plot(x_new, power_smooth,color='green', label='n=5')
#         # plt_show('n = 5')
#     elif n == 10:
#         x = np.arange(a,b,0.02)
#         plt.plot(x,ln(x),color='red', label='n=10')
#         # plt_show('n = 10')
#     elif n == 15:
#         x_new = np.linspace(T.min(), T.max(), 10000)
#         plt.plot(x_new, ln(x_new),color='yellow', label='n=15')
#
#         # plt_show('n = 15')

x1,y1 = init_array(L[0])
x2,y2 = init_array(L[1])
x3,y3 = init_array(L[2])
n1 = len(x1) -1
n2 = len(x2) -1
n3 = len(x3) -1
ln_1 = sum(ln_sum(x1,y1))
ln_2 = sum(ln_sum(x2,y2))
ln_3 = sum(ln_sum(x3,y3))
ln_y1 = ln_1(x1)
ln_y2 = ln_2(x2)
ln_y3 = ln_3(x3)
T = np.array(x1)
x_new1 = np.linspace(T.min(),-0.2,200)
x_new2 = np.linspace(0.2,T.max(),200)
Fix_p = np.poly1d(0,0,0.4326)
ln_y11 = ln_y1 + Fix_p
power1 = np.array(ln_1(x_new1))
power2 = np.array(ln_1(x_new2))
plt.plot(x_new1,power1,color='green',label='n=5')
plt.plot(x_new2,power2,color='green',label='n=5')
# x_new3_ = np.array([-1/5,0,1/5])
# x_new3 = np.linspace(x_new3_.min(),x_new3_.max(),200)
# g_x_new = 5*np.pi/3*x_new3
# power3_ = ln_1(x_new3) * np.cos(g_x_new) *2
# plt.plot(x_new3,power3_,color='green',label='n=5')
# x = np.arange(a,b,0.02)
# T = np.array(x3)
# x_new = np.linspace(T.min(), T.max(), 10000)
# plt.plot(x,ln_2(x),color='red', label='n=10')
# plt.plot(x_new, ln_3(x_new),color='yellow', label='n=15')
x = np.linspace(-1,1,1000)
y = 1 + 25 * x * x
plt.plot(x,1/y,color="red",label='function')
plt.legend()
plt_show()