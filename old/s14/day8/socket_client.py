import socket

client_conn_host = '192.168.36.138'
client_conn_port = 7001

client = socket.socket()
client.connect((client_conn_host,client_conn_port))

