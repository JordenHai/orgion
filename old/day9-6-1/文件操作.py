
#data = open('yesterday',encoding="utf-8").read()
f = open("yesterday",'r',encoding="utf-8")
#文件句柄(文件的起始位置)
f2 = open("yesterday2","w",encoding="utf-8")
#
f3 = open("yesterday2","a",encoding="utf-8")
#

data = f.read()

print(data)

