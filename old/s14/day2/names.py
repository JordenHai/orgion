# -*- coding:utf-8 -*-
# Author: Jorden Hai
import copy
names = ["ZhangYang","GuYun","XuLiangchen",['alex','jack'],"YangZhe","ChenZhonghua","ZhaoZi"]

print(names[::2])

for i in names[::2]:
    print(i)

'''
names2 = copy.deepcopy(names)

names[1] = '向鹏'
print(names)
print(names2)

names[3][0] = 'Alex'
names2[3][1] = 'Jack'
'''
#浅层次的copy
#只对第一层进行copy
#其他层次就是复制下
#对于列表中的列表 copy动作只是复制了其指针！！
#真正的复制

'''
names.append("YangZhe")
names.append("LeiHaidong")
names.insert(1,"ChenZhonghua")
names.insert(3,"ZhaoZi")
names[2] = 'XieDi'
print(names[names.index("XieDi")])
names.append("ChenZhonghua")
print(names.count('ChenZhonghua'))
count = 0
for name in names:
    if name == "ChenZhonghua":
        count = count +1
print(count)
print(names)
names.reverse()
names.sort() #ASCII码排序
names.extend(names2)
del names[1]
names.pop(1)
names.remove("XieDi")
names.pop(1)
names.remove("ZhangYang")
newnames = names.copy()
print(newnames)
print(enumerate(names))
for index,value in enumerate(names):
    print(index,value)
print(names[len(names)-1])
print(names[-1])
print(names[-2:])
'''

