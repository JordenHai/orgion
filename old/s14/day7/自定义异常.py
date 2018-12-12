
class AlexException(Exception):
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise AlexException('我的异常')
except AlexException as e:
    print(e)