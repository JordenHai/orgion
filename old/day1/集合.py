


list_1 = [1,4,5,6,9,7,3,1,2]

list_1 = set(list_1)

print(list_1)

list_2 = set([2,6,0,66,22,8,4])

print(list_2)

#交集
list_3 = list_1.intersection(list_2)

print(list_3)

#并集
list_3 = list_1.union(list_2)

print(list_3)

#差集
list_3 = list_1.difference(list_2)

print(list_3)

list_3 = list_2.difference(list_1)

print(list_3)

#子集
#判断是不是子集
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))
list_3 = set([1,3,7])
print(list_3.issubset(list_1))
print(list_1.issuperset(list_3))

#反向的差集
#对称差集
list_3 = list_1.symmetric_difference(list_2)
#去掉大家都有的
print(list_3)
L = []
for value in list_3:
    L.append(value)

print(L)

#disjoint

list_3 = [22,44,55]

print(list_1.isdisjoint(list_3))

#用运算符来计算交并

print(list_1&list_2)#交集
print(list_1|list_2)#并集
print(list_1-list_2)#差集
print(list_1^list_2)#对称差集

#subset and upperset
#没有专门符号


print(list_1)
list_1.add(99)
print(list_1)
list_1.update([88,99,66,33])
print(list_1)
list_1.remove(1)
print(list_1)

