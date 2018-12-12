import socket
import threading
import queue
import os
import re

server_Host = 'localhost'
server_Port = 7400
server_Port_1 = 7401

L = {}


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
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", msg):
        recv_msg = "IP vaild -ip" + msg
        p.put(recv_msg)
        print(recv_msg)
        command = 'ifconfig ens33 ' + msg + ' netmask 255.255.255.0'
        os.popen(command)
        res = os.popen('ifconfig').read()
        print(res)
    else:
        recv_msg = "IP invaild -ip"
        p.put(recv_msg)
        print(recv_msg)

    return 0


def Application_Conf_ru(msg):
    # 精确的匹配给定的字符串是否是IP地址
    route_des = msg.split('*')[0]
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                route_des):
        #       recv_msg = "IP vaild -Ru"
        #       p.put(recv_msg)
        route_des = msg.split('*')[0]
        route_gw = msg.split('*')[1]
        command = 'route add ' + route_des + ' gw ' + route_gw
        os.popen(command)
        command1 = 'route -n|grep ' + route_des
        res = os.popen(command1).read()
        p.put(res)
        print(res)
    else:
        recv_msg = "IP invaild -Ru"
        p.put(recv_msg)
        print(recv_msg)


def Application_Conf_co(msg):
    ip_command = msg.split('*')[0]
    command = msg.split('*')[1]
    key = msg.split('*')[2]
    L[ip_command] = command
    command = command.upper()
    if command == 'DROP':
        command = 'iptables -I INPUT -s ' + ip_command + '/32 -j DROP'
        res = os.popen(command)
        res = os.popen('iptables -L -n').read()
        p.put(res)
    elif command == 'ACCEPT':
        command = 'iptables -L --line-numbers' + '|grep ' + ip_command
        res = os.popen(command).read()
        if res:
            command = 'iptables -D INPUT ' + res[0]
            os.popen(command)
            command = 'iptables -L --line-numbers'
            res = os.popen(command).read()
            p.put(res)
        else:
            command = 'iptables -I INPUT -s ' + ip_command + '/32 -j ACCEPT'
            res = os.popen(command)
            res = os.popen('iptables -L -n').read()
            p.put(res)
    elif command == 'REJECT':
        command = 'iptables -t filter -A INPUT -s ' + ip_command + '/32 -j REJECT'
        os.popen(command)
        command = 'iptables -L -n'
        res = os.popen(command).read()
        p.put(res)


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

t1 = threading.Thread(target=socket_client_recv, args=(q,))

t2 = threading.Thread(target=func, args=(q,))

t3 = threading.Thread(target=socket_client_send, args=(p,))

t2.setDaemon(True)

t1.start()
t2.start()
t3.start()

