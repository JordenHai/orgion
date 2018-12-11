#-*- coding:utf-8 -*-

import time
user,passwd = 'alex','abc123'

def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'local':
                username = input("Username:").strip()
                password = input("password:").strip()
                if user == username and passwd == password:
                    print("\033[0;37;42mUser has passed authentication\033[0m")
                    # print("\033[0;37;41m\t方倍实验室\033[0m") 红色
                    # print("\033[0;37;42m\t方倍实验室\033[0m") 绿色
                    # res = func(*args,**kwargs)  #执行结果没有返回值
                    print("Afer authencation")
                    # return res
                else:
                    exit("\033[0;37;41mInvalid username or password uncorrect\033[0m")
            elif auth_type == 'ldap':
                print("Ldap is not suittable for us to operat")
        return wrapper
    return outer_wrapper

# 最外层的只是传 装饰器的参数 直接执行 outer_wrapper
# 内两层 和基本的一样
#
def web_index():
    print("welcome to the index")
    pass

#
#
@auth(auth_type = 'local')
def web_home():  #home() = wrapper()
    print("welcome to home")
    return "from home"
# 加上装饰器，在编译的时候，会先解释 会解释道 wrapper 也就是 home = wrapper 这个阶段
@auth(auth_type = 'ldap')
def web_bbs():
    print("welcome to bbs")
    pass

web_index()
web_home()
web_bbs()

# 现在支持一种
# 我们现在要支持多种
