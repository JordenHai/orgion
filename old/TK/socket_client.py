import socket
import threading
import queue
import os
import re

server_Host = 'localhost'
server_Port = 7351
server_Port_1 = 7352

L = {}
L_Index = {}

def socket_client_recv(q):
    client = socket.socket()
    client.connect((server_Host, server_Port))
    while True:
        f = open("D:\own.txt", 'ab+')
        f_l = open("D:\limit.txt", 'wb+')
        data = client.recv(124000)
        print(type(data))
        q.put(data)
        print(data)
        f.write(data)
        f_l.write(data)
        f.close
        f_l.close


def socket_client_send(p):
    client_send = socket.socket()
    client_send.bind((server_Host, server_Port_1))
    client_send.listen(5)
    conn, addr = client_send.accept()
    print(conn, addr)
    while True:
        if not p.empty():
            msg = p.get()
            print(".........")
            conn.send(msg.encode('utf-8'))

    client_send.close()



def Application_Conf_ip(msg):
    # 精确的匹配给定的字符串是否是IP地址
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",msg):
        recv_msg = "IP vaild -ip"+msg
        p.put(recv_msg)
        print(recv_msg)
        command = 'ifconfig ens33 '+msg+' netmask 255.255.255.0'
        # os.popen(command)
        # res = os.popen('ifconfig').read()
        # print(res)
    else:
        recv_msg = "IP invaild -ip"
        p.put(recv_msg)
        print(recv_msg)

    return 0


def Application_Conf_ru(msg):
    # 精确的匹配给定的字符串是否是IP地址
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", msg):
#       recv_msg = "IP vaild -Ru"
#       p.put(recv_msg)
        route_des = msg.split('*')[0]
        route_gw = msg.split('*')[1]
        # command = 'route add '+route_des+' gw '+route_gw
        # os.popen(command)
        # command1 = 'route -n|grep '+route_des
        # res = os.popen(command1).read()
        # p.put(res)
        # print(res)
    else:
        recv_msg = "IP invaild -Ru"
        p.put(recv_msg)
        print(recv_msg)


def Application_Conf_co(msg):
    # 精确的匹配给定的字符串是否是IP地址
   # recv_msg = "Recieve!"
   # p.put(recv_msg)
   # print(recv_msg)
    command = msg.split('*')[1]
    ip_command = msg.split('*')[0]
    L[ip_command] = command
    if ip_command not in L_Index:
        L_Index[ip_command] = msg.split('*')[2]
    else:
        key = int(L_Index.get(ip_command))
    print(L)
    print(L_Index)
    command = command.upper()
    if command == 'DROP':
        command = 'iptables -I INPUT -s '+ip_command+'/32 -j DROP'
        res = ip_command+' DROP'
        p.put(res)
        # res = os.popen(command)
        # res = os.popen('iptables -L -n').read()
        # p.put(res)
    elif command == 'ACCEPT':
        command = 'iptables -D INPUT '+str(len(L_Index)-key+1)
        # command = 'iptables -L -n'
        print(command)
        # res = os.popen(command).read()
        # p.put(res)



def Application(msg):
    if msg[:2] == 'ip':
        msg = msg[2:]
        print(msg)
        msg = Application_Conf_ip(msg)
    elif msg[:2] == 'ru':
        msg = msg[2:]
        msg = Application_Conf_ru(msg)
    elif msg[:2] == 'co':
        msg = msg[2:]
        msg = Application_Conf_co(msg)
    return msg


def func(q):
    while True:
        if not q.empty():
            msg = q.get()
            print(type(msg))
            msg = msg.decode()
            Application(msg)


q = queue.Queue()

p = queue.Queue()

t1 = threading.Thread(target=socket_client_recv,args=(q,))

t2 = threading.Thread(target=func,args=(q,))

t3 = threading.Thread(target=socket_client_send,args=(p,))

t2.setDaemon(True)

t1.start()
t2.start()
t3.start()