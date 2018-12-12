
import threading
import queue
def fun1(q):
    while True:
        a = input()
        q.put(a)

def fun2(q):
    while True:
        if not q.empty():
            a = q.get()
            print(a)

q = queue.Queue()

t1 = threading.Thread(target=fun1,args=(q,))

t2 = threading.Thread(target=fun2, args=(q,))
t2.setDaemon(True)

t1.start()
t2.start()

