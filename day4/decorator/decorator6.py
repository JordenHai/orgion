#-*- coding:utf-8 -*-

import time
user,passwd = 'alex','abc123'

def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username:").strip()
        password = input("password:").strip()
        if user == username and passwd == password:
            print("\033[0;37;42mUser has passed authentication\033[0m")
            # print("\033[0;37;41m\t方倍实验室\033[0m") 红色
            # print("\033[0;37;42m\t方倍实验室\033[0m") 绿色
            res = func(*args,**kwargs)  #执行结果没有返回值
            print("Afer authencation")
            return res
        else:
            exit("\033[0;37;41mInvalid username or password uncorrect\033[0m")
    return wrapper

def web_index():
    print("welcome to the index")
    pass

@auth
def web_home():
    print("welcome to home")
    return "from home"

@auth
def web_bbs():
    print("welcome to bbs")
    pass

web_index()
print(web_home())
web_bbs()

# 现在支持一种
# 我们现在要支持多种
