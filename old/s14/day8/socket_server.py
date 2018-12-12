import socket

server_host = 'localhost'
server_port = 7000


server = socket.socket()
server.bind((server_host,server_port))

server.listen()

while True:
    conn,addr = server.accept() #阻塞

    while True:
        print('New Connetion',addr)
        data = conn.recv(1024) # 8192 recv默认是阻塞的
        if not data:
            break
        else:
            print(data)            #
            conn.send(data.upper())#客户端一旦断开就死循环 因为会认为接收到为空数据，死循环

