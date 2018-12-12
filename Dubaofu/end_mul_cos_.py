#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
round_num = 8 #小数位数
a = -1        #数组起点
b = 1         #数组终点
L = [5,10,15,20,0]#分割次数
l_set = { 5:['black','n = 5'], \
         10:['yellow', 'n = 10'], \
         15:['blue', 'n = 15'], \
         20:['green', 'n = 20'], \
          0:['red', 'Function']}

#初始化数组（cos），自变量和因变量
def init_array(n):
    list_x = []
    list_y = []
    for i in range(n + 1):
        num = np.pi * i /n
        num = np.cos(num)
        num = round(num, round_num)
        num = float(num)
        list_x.append(num)
    for i in range(n + 1):
        num = 1 / (1 + 25 * list_x[i] * list_x[i])
        num = round(num, round_num)
        list_y.append(num)
    return list_x, list_y
    pass

#计算 Wn+1(x) PS:但缺少（X-Xk）项
def W_new_1(num, num_t):
    ploy_sum = 1
    n = len(num) -1
    for i in range(n + 1):
        if i == num_t:
            continue
        else:
            ploy_sum = np.poly1d([0, 1, -num[i]]) * ploy_sum
    return ploy_sum

#计算W`n+1(x) PS:只有常数项。没有（X - Xk）项
def W_new(num,num_t):
    ploy_sum = 1
    n = len(num) -1
    for i in range(n + 1):
        if i == num_t:
            continue
        else:
            ploy_sum = round(ploy_sum * (num[num_t] - num[i]), round_num)
    return ploy_sum

#ln_sum 计算Wn+1(x)/W`n+1(x)*Yk的值
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

#显示图例
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

#生成函数及其图像
def get_plot(l):
    for index,i in enumerate(l):
        if index < 4:
            x,y = init_array(i)
            ln = sum(ln_sum(x,y))
            T = np.array(x)
        else:
            T = np.array([-1,1])

        if i == L[0]:
            x_new = np.linspace(T.min(), T.max(),500)
            ln_y = ln(x_new)
            plt.plot(x_new,ln_y,color = l[i][0],label = l[i][1])
        elif i == L[2]:
            x_new = np.linspace(T.min(), T.max(), 5000)
            ln_y = ln(x_new)
            plt.plot(x_new, ln_y, color=l[i][0], label=l[i][1])
        elif i == L[1]:
            x_new = np.arange(T.min(), T.max(),0.02)
            ln_y = ln(x_new)
            plt.plot(x_new,ln_y,color = l[i][0],label = l[i][1])
        elif i == L[4]:
            x_new = np.linspace(T.min(),T.max(),1000)
            ln_y =1 + 25 * x_new**2
            plt.plot(x_new,1/ln_y,color = l[i][0],label = l[i][1])
        else:
            x_1 = np.arange(T.min(),-0.25,0.01)
            x_2 = np.arange(-0.25,0.25,0.001)
            x_3 = np.arange(0.25,T.max(),0.01)
            x_new = np.concatenate((x_1,x_2,x_3),axis=0)
            ln_y = ln(x_new)
            print(type(ln_y))
            plt.plot(x_new,ln_y,color = l[i][0],label = l[i][1])
    pass

get_plot(l_set)
plt.legend()
plt_show()