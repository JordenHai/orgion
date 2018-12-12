# -*- coding:utf-8 -*-
# Author: Jorden Hai

#客户端
import socket

client = socket.socket() #声明socket类型 同时生成socket连接对象
client.connect(('localhost',6969))

#client.send(b"fhsdkjfhalf;")
while True:

    msg = input(">>:").strip()
    if len(msg) == 0:

        continue

    client.send(msg.encode('utf-8'))
    data = client.recv(102400)#只能比特流 每次结收的数据量是有限的！不同系统 不同大小
    print("recv:",data.decode())

client.close()
