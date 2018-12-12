# -*- coding:utf-8 -*-
# Author: Jorden Hai

#服务器
import socket
import os

# res = os.popen(data).read()
# res 存在缓存区里面
#

server = socket.socket()
server.bind(('192.168.36.132',6969))#绑定端口
server.listen(5)#监听端口

while True:
    print("等待电话进入")
    conn,addr = server.accept() #等待电话打进
    print(conn,addr)
    #conn 客户端连接过来，从而在服务器端为其生成的一个实例
    while True:
        print("电话打进去")
        data = conn.recv(1024)
        if data.decode == 'q':
            print("client has lost!")
            break
        else:
            print("recv:",data.decode())
            #执行动作
            #res = os.popen(data).read()
            #
            conn.sendall(data.upper())

server.close()

