
# data = open("yesterday",encoding = 'utf-8').read()
# f = open("yesterday",encoding = 'utf-8')
# f 又称文件句柄 就是文件的内存对象 文件的位置 大小 字符集
# data = f.read()
# data2 = f.read()
# print(data)
# print("----------------")
# print(data2)
#
# f.close()
# 其实f在read中，是以指针方式再往下读取数据
# 读完一遍，指针已经到了底部了
# 所以没有数据可以读取

f = open("yesterday",encoding = 'utf-8')
#
# for i in range(5):
#     print(f.readline())
# 读取多行

# print(f.readlines())
#
# for line in f.readlines():
#     print(line)

# 使之索引化
# enumerate()
#简单循环
# for index,line in enumerate(f.readlines()):
#     if index == 9:
#         print("---分割线---")
#         continue
#     print(line.strip())

# the code level is high
# count = 0
# for line in f:
#     count = count + 1
#     if count == 10:
#         print("----=---------=----")
#         continue
#     print(count)
#     print(line)

# f.tell() == 是指文件指针位置
# f.seek(nums) == 到指定位置 一般默认为0
# print(f.tell())
# data = f.readline()
# print(f.tell())
# num_1 = f.seek(0)
# num_2 = f.tell()
# print(num_1,num_2)
# f.readline()
# num_3 = f.tell()
# print(num_3)


# print(f.encoding)
#
# print(f.seekable())
# print(type(f.seekable()))
# if f.seekable() == True:
#     print(1)

# 写入操作
# 我不是每写一行 就写入硬盘
# 操作系统等到缓存满了，才会一次性写入
# f.flush 的作用等于强制刷新
# print(f.flush())



 




f.close()