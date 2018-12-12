
class Gui_socket(object):
    def __init__(self,server_host,server_port):
        self.host = server_host
        self.port = server_port
        self.sever = None
        self.conn = None
        self.addr = None
    def runc(self):
        self.sever = socket.socket()
        self.sever.bind(self.host,self.port)
        self.sever.listen(5)
        self.conn,self.addr = self.sever.accept()
    def sent_message(self,data):
        if isinstance(data,(bytes,)):
            self.conn.send(data)
        else:
            self.conn.send(data.encode())


class Niu(object):


    def __init__(self):
