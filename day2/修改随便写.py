f = open('yesterday2','wb')

# data = f.read().decode('utf-8')
data1 = 'hello binary'
data1 = data1.encode()
f.write(data1)
# print(data)