#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
round_num = 8 #小数位数
a = -1        #数组起点
b = 1         #数组终点

#初始化数组，自变量和因变量
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

L = [5,10,15,20]
x1,y1 = init_array(L[0])#初始化n = 5
x2,y2 = init_array(L[1])#初始化n = 10
x3,y3 = init_array(L[2])#初始化n = 15
x4,y4 = init_array(L[3])#初始化n = 20
ln_1 = sum(ln_sum(x1,y1))#生成Ln(x)函数
ln_2 = sum(ln_sum(x2,y2))#生成Ln(x)函数
ln_3 = sum(ln_sum(x3,y3))#生成Ln(x)函数
ln_4 = sum(ln_sum(x4,y4))#生成Ln(x)函数
ln_y1 = ln_1(x1)#计算L(x)的初值
ln_y2 = ln_2(x2)#计算L(x)的初值
ln_y3 = ln_3(x3)#计算L(x)的初值
ln_y4 = ln_4(x4)#计算L(x)的初值

T = np.array(x1)#将x1的值转换成矩阵
x_1 = np.linspace(T.min(), T.max(),500)#在矩阵的最大最小之间插入500个值
ln_y1 = ln_1(x_1)#计算新的ln_y的值
power1 = np.array(ln_y1)#生成ln_y1的矩阵
plt.plot(x_1, power1,color='green',label='n=5')#画出图像

T = np.array(x2)#将x2的值转换成矩阵
x_2 = np.arange(T.min(),T.max(),0.02)#在数轴上以0.02分割生成矩阵
ln_y2 = ln_2(x_2)#计算新生产的ln_y值
plt.plot(x_2,ln_y2,color='red', label='n=10')#画出图像

T = np.array(x3)#将x3的值转换成矩阵
x_3 = np.linspace(T.min(),T.max(),500)#在矩阵的最大最小之间插入500个值
ln_y3 =  ln_3(x_3)#计算新生产的ln_y值
plt.plot(x_3,ln_y3,color='yellow', label='n=15')#画出图像

T = np.array(x4)#将x4的值转换成矩阵
x_4 = np.arange(T.min(),T.max(),2/6)#在数轴上以1/3分割生成矩阵
ln_y4 =  ln_4(x_4)#计算产生的新ln_y值
plt.plot(x_4,ln_y4,color='black',label='n=20')#画出图像

x = np.linspace(a,b,1000)#将在[a,b]上生成1000个点
y = 1 + 25 * x * x#计算新生产的y值
plt.plot(x,1/y,color="red",label='function')#画出图像

plt.legend()
plt_show()