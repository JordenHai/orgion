from tkinter import *
import threading
import queue
import socket
import time
server_Host = 'localhost'
server_Port = 7351
server_Port_1 = 7352

class Reg(Frame):

    def __init__(self,master,q,p):
        self.frame = Frame(master)
        self.frame.pack()
        self.status = 'static'
        self.createWidgets()
        self.q = q
        self.p = p
        self.num = 1

    def createWidgets(self):
        '''IP Configure'''
        self.lab11 = Label(self.frame, text="IP Configur:")
        self.lab11.grid(row=0, column=0, sticky=E+W+N+S)

        self.lab12 = Label(self.frame,text='')
        self.lab12.grid(row=0, column=2, sticky=E+W+N+S)
        '''IP Input ...'''
        self.ent11 = Entry(self.frame)
        self.ent11.grid(row=0, column=1, sticky=W)



        '''Add Route...'''
        self.lab21 = Label(self.frame, text="Add Route:")
        self.lab21.grid(row=1, column=0, sticky=E+W+N+S)
        '''Route Input.'''
        self.ent21 = Entry(self.frame)
        self.ent21.grid(row=1, column=1, sticky=W)
        self.ent22 = Entry(self.frame)
        self.ent22.grid(row=1, column=2, sticky=W)

        '''Iptables Suggestion...'''
        self.lab31 = Label(self.frame, text="Iptables_Des:")
        self.lab31.grid(row=2, column=0, sticky=E+W+N+S)
        self.lab32 = Label(self.frame, text="")
        self.lab32.grid(row=3, column=0, columnspan =2, sticky=W)
        self.lab33 = Label(self.frame,text='')
        self.lab33.grid(row=4, column=0,columnspan =2, sticky=W)

        '''Iptables Suggestion。。。'''
        self.ent31 = Entry(self.frame)
        self.ent31.grid(row=2, column=1, sticky=W)
        self.ent32 = Entry(self.frame)
        self.ent32.grid(row=2, column=2, sticky=W)



        '''Send.....'''
        self.button3 = Button(self.frame, text="Send", command=self.Send)
        self.button3.grid(row=0, column=3, sticky=E+W+N+S)
        '''Add_....'''
        self.button4 = Button(self.frame, text="Add_", command=self.Add_Route)
        self.button4.grid(row=1, column=3, sticky=E+W+N+S)
        '''Confirm....'''
        self.button4 = Button(self.frame, text="Conf", command=self.Confirm)
        self.button4.grid(row=2, column=3, sticky=E+W+N+S)

    def Submit(self):
        s1 = self.ent11.get()
        # s2 = self.ent2.get()
        # if s1 == 'freedom' and s2 == '123':
        #     self.lab3["text"] = "Confirm"
        # else:
        #     self.lab3["text"] = "Error!"
        # self.ent1.delete(0,len(s1))
        # self.ent2.delete(0elf.p.empty():
        #         #     self.lab4['*****'] = self.p.get()
        #              #     self.ent1.delete(0,len(s1)),len(s2))
        # if not s
    def Send(self):
        msg = self.ent11.get()
        msg = 'ip' + msg
        self.q.put(msg)
        msg = self.p.get().decode()
        print(msg)
        self.status = msg
        self.lab12['text'] = self.status

    def Add_Route(self):
        msg_route = self.ent21.get()+'*'+self.ent22.get()
        msg_route = 'ru'+msg_route
        self.q.put(msg_route)
        massage = self.p.get().decode()
        print(massage)
        self.status = massage
        '''
        目标            网关            子网掩码        标志  跃点   引用  使用 接口
        0.0.0.0         192.168.36.2    0.0.0.0         UG    100    0        0 ens33
        169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 ens33
        192.168.360.000 192.168.360.000 192.168.360.000 U     100    0        0 ens33
        '''
        title = '目标            网关            子网掩码        标志  跃点   引用  使用 接口'
        self.lab32['text'] = title
        self.lab33['text'] = self.status

    def Confirm(self):
        msg_ip = self.ent31.get()
        msg_ce = self.ent32.get()
        msg_all = 'co'+msg_ip +'*'+ msg_ce+'*'+str(self.num)
        self.num = self.num + 1
        print(msg_all)
        self.q.put(msg_all)


def Gui_server(q):
    root = Tk()
    root.title("SDN Controller")
    app = Reg(root,q,p)
    root.mainloop()

def socket_server(q):
    server = socket.socket()
    server.bind((server_Host,server_Port))
    server.listen(5)
    conn, addr = server.accept()
    print(conn, addr)
    while True:
        if not q.empty():
            msg = q.get()
            conn.send(msg.encode('utf-8'))
    server.close()

def socket_server_recv(p):
    server_recv = socket.socket()
    server_recv.connect((server_Host, server_Port_1))
    while True:
        data = server_recv.recv(124000)
        p.put(data)
        print(data.decode())


q = queue.Queue()

p = queue.Queue()

t1 = threading.Thread(target=Gui_server,args=(q,))

t2 = threading.Thread(target=socket_server, args=(q,))

t3 = threading.Thread(target=socket_server_recv,args=(p,))

t2.setDaemon(True)

t1.start()
t2.start()
time.sleep(10)
t3.start()