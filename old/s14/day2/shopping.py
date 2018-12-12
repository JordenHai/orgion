# -*- coding:utf-8 -*-
# Author: Jorden Hai
'''
your salary:5000
1. Iphone           5800
2. Mac Pro          12000
3. Starbuck Latte   31
4. Alex Python       81
5. Bike             800
added [Iphone] to your Shopping Car!!
You
1. Iphone           5800
2. Mac Pro          12000
3. Starbuck Latte   31
4. Alex Pythn       81
5. Bike             800
have bought below:
[[iphone,5800],[bike,800]]
your balance : ...
'''
goodslist = [('Iphone',5800),('Mac Pro',12000),('Starbuck Latte',31),('Alex Python',81),('Bike',800)]
goods = []
own_list = []
def showlist(L):
    for index,value in enumerate(L):
        print("%d. %-15s  %-5.0d"%(index+1,value[0],value[1]))

def joinownlist(chose):
    chose = chose -1
    goods.append(goodslist[chose])
    own_list.extend(goods)
    goods.clear()

def count(chose,salary):
    chose = chose - 1
    if salary >= goodslist[chose][1]:
        salary = salary - goodslist[chose][1]
        return salary
    else:
        return salary

own_salary = int(input("Input your salary:"))


goodslist.sort()
while True:
    print("Welcome to Shop!")
    showlist(goodslist)
    chose = input("Input what your want:")
    if chose.isdigit():
        chose = int(chose)
        if chose <= len(goodslist) and chose > 0:
            salary = count(chose,own_salary)
            print("aaaaa", salary)
            print("bbbbb", own_salary)
            if salary == own_salary:
                print("1233333321")
                print("你的余额只剩[%-4d]啦"%own_salary)
            else:
                own_salary = salary
                print("ccccc", own_salary)
                joinownlist(chose)
                print("added \033[31;1m[%s]\033[0m to your shopping car,your current balance is \033[31;1m%4d\033[0m"%(goodslist[chose-1][0],own_salary))
    elif chose == 'q':
        break
    else:
        print("invalid option")


print('Have bought below:')
showlist(own_list)
print("Your balance : %-4d"%own_salary)

