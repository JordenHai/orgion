import os
import re

def Application_Conf_ip(msg):
    # 精确的匹配给定的字符串是否是IP地址
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",msg):
        recv_msg = "IP vaild"
        p.put(recv_msg)
        print(recv_msg)
    else:
        recv_msg = "IP invaild"
        p.put(recv_msg)
        print(recv_msg)

    return 0

def Application_Conf_ru(msg):
    # 精确的匹配给定的字符串是否是IP地址
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", msg):
        recv_msg = "IP vaild"
        print(recv_msg)
    else:
        recv_msg = "IP invaild"
        print(recv_msg)

def Application_Conf_co(msg):
    pass



def Application(msg):
    if msg[:2] == 'ip':
        msg = msg[2:]
        print(msg)
       # msg = Application_Conf_ip(msg)
    elif msg[:2] == 'ru':
        msg = msg[2:]
    elif msg[:2] == 'co':
        msg = msg[2:]
    return msg

