# -*- coding:utf-8 -*-
# Author: Jorden Hai

#调用系统模块
import os

cmd_res = os.system("dir")#输出到屏幕上了 执行命令 结果不保存
print("-->",cmd_res) #cmd_res 值为0代表了成功

#把东西保存到某地址
cmd_res = os.popen("dir")
print("-->",cmd_res)

#加上 .read()方法读出
cmd_res = os.popen("dir").read()
print("-->",cmd_res)

#创建目录
os.mkdir("new_dir")