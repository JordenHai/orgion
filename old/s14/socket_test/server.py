
import socket
import os
import tkinter as tk

server = socket.socket()
server.bind(('localhost',7323))
server.listen(5)
conn,addr = server.accept()
print(conn,addr)
print("-------*-------0")
while True:

    msg = input("-->:").strip()
    if len(msg) == 0:
        continue
    conn.send(msg.encode('utf-8'))
server.close()
