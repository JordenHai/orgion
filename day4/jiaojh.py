#-*- coding:utf-8 -*-

def func_name(arg1,arg2,arg3,*args,**kwargs):
    pass

func_name(4,5,6,9,7,8,5,name='alex')
#   4，5，6，（9，7，8，5），{‘name‘：'alex'}

age = 22
name = ['alex','xiaom']
def change_age(num1):
    global age
    age = num1
    name.append('112')
    print(name)
    print(age)
    pass

print(name)
change_age(23)
print(name)
print(age)

# 递归要有明确的结束条件
#问题规模每递归一次都应该比上一次的规模减少
# 效率低

# 高阶函数

# 把一个函数当成参数 传去进去
# 真真正正的函数式编程不会有参数的


