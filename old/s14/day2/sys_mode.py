# -*- coding:utf-8 -*-
# Author: Jorden Hai

import sys
import login

#打印环境变量
#print(sys.path)
print(sys.argv)
#print(sys.argv[2])

#导入时 sys 时 会先到当前目录下找
#在python2中会出错的
#['C:\\Users\\焦海\\PycharmProjects\\s14\\day2',
# 'D:\\python3\\python37.zip',
# 'D:\\python3\\DLLs',
# 'D:\\python3\\lib',一般标准库
# 'D:\\python3',
# 'D:\\python3\\lib\\site-packages'] 一般第三方库在此路径霞