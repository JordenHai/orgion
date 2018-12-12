# -*- coding:utf-8 -*-
# Author: Jorden Hai
#秘文输入
import getpass
#新的包
_username = 'jh'
_password = '123456'
username = input("username:")
password = input("password:")

if username == _username and _password == password:
    print("Success Login!")
    print('''Wellcome user {_name} login...'''.format(_name = username))
else:
    print("Fail")
