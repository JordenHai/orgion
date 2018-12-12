#-*- coding：utf-8 -*-

import socket
import os
server_host = 'localhost'
server_port = 7005

server = socket.socket()
server.bind((server_host,server_port))
server.listen(5)

while True:
    conn,addr = server.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            data = data.decode()
            print('执行指令：',data)
            cmd_res = os.popen(data).read()
            conn.send(cmd_res.encode('utf-8'))

server.close()
