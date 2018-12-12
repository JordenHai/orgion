import time
import string
from functools import reduce
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print ('[%s] %s()...' % (prefix, f.__name__))
            return f(*args, **kw)
        return wrapper
    return log_decorator

def performace(unit = 'ms'):
    def per_decorator(f):
        def wrapper(*args,**kw):
            t1 = time.time()
            runfunc = f(*args,**kw)
            time.sleep(0.000002)
            t2 = time.time()
            if unit == 's':
                t = t2 - t1
                print("call %s() consume %f %s"%(f.__name__,t,unit))
            elif 'ms' == unit:
                t = t2 - t1
                t = t * 1000
                print("call %s() consume %f %s" % (f.__name__, t, unit))
            return runfunc
        return wrapper
    return  per_decorator

def logger(f):
    def lag_wrapper(*args,**kw):
        print('call %s()...'%(f.__name__))
        return f(*args,**kw)
    return lag_wrapper


def func(x,y):
    return x*y

@performace()
def factories(n):
    return reduce(func,range(1,n+1))

print(factories(10))
