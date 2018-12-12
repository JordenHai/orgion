#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
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
#
# x = np.linspace(-2 * np.pi,2 * np.pi,200)
# y1,y2 = np.sin(x),np.cos(x)
# y3 = np.sin(x) * 0
#
# plt.plot(x,y1)
# plt.plot(x,y2)

x = [4,4.2,4.5,4.7,5.1,5.5,5.9,6.6,6.8,7.1]
y = [102.56,113.18,130.11,142.05,167.53,195.14,224.87,\
     256.73,299.50,326.72]
x_index= ['First','Second','Third','Fourth'\
          ,'Fifth','Sixth','Seventh','Eighth'\
          ,'Ninth','Tenth']
x_mark = ['x','+',"o",'x','+',"o",'x','+',"o",'x']
def plt_splash(num_x,num_y,label_1,mark = 'x',hue = 'red',size = 40):
    plt.scatter(num_x,num_y,marker=mark,color=hue,s = size\
                ,label=label_1)
    pass

for i in range(10):
    plt_splash(x[i],y[i],label_1=x_index[i],mark = x_mark[i])
    pass

plt_show()