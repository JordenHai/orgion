import socket
import os

server_Host = 'localhost'
server_Port = 7343

client = socket.socket()
client.connect((server_Host,server_Port))
data_empty = ''
data_empty = data_empty.encode()

while True:
    print("------------------------")
    f = open("D:\own.txt",'ab+')
    f_l = open("D:\limit.txt",'wb+')
    data =  client.recv(124000)
    print(type(data))
    f.write(data)
    f_l.write(data)
    f.close
    f_l.close
    print("------------------------")

client.close()
