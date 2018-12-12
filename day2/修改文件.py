# # 没什么调用
# f = open('yesterday2','w+',encoding='utf-8')
# # 创建的为新文件
# # 写依旧是正常按顺序写，读依旧正常读
# f.write('----------\n')
# #10+2 = 12
# f.write('----------\n')
# #12+12 = 24
# f.write('----------\n')
# #36
# f.write('----------\n')
# #48
# f.write('----------\n')
# #60
# f.write('----------\n')
# #72
# f.write('----------\n')
# #84
# f.write('----------\n')
# #96
# f.write('----------')
# #106
# print(f.tell())
# f.seek(13)
# print(f.readline())
# f.write("should be at the second line")
# f.close()
# 效果依旧在最后追加
'''
# 读写模式还是有一些用处的
f = open('yesterday2','r+',encoding='utf-8')
# 是以读和追加方式打开的文件
#读是正常读 写是追加到文件最后
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
# 这个方式是追加
f.write("-----------")

print(f.readline())

f.close()
'''
