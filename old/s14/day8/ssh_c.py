#-*- coding：utf-8 -*-

import socket
client_host = 'localhost'
client_port = 7005

client = socket.socket()

client.connect((client_host,client_port))

while True:

    cmd = input('>>:').strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))
    cmd_res = client.recv(1024)
    cmd_res = cmd_res.decode()
    print(cmd_res)

client.close()