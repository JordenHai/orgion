# -*- coding:utf-8 -*-
# Author: Jorden Hai

class Role(object):

    globle_resu = {
        'plice':[],
        'terrorist':[],
    }

    n_list = []

    def __init__(self,name,role,weapon,life_value = 100,money=10000):
        self.name = name  #实例变量 （静态属性） 作用域就是实例本身
        self.role = role
        self.weapon  = weapon
        self.__life_value = life_value
        self.money = money
        #构造函数
        #在实例化时，做一些类的初始化操作

    def __shot(self): #类的方法 功能 （动态属性）
        print("shorting")

    def show_status(self):
        print("name:%s life_value:%s"%(self.name,self.__life_value))

    def __del__(self): #析构函数 程序结束的时候的扫尾工作
        pass
        #print("%s 彻底死了。。。"%self.name)

    def got_shot(self):
        self.__life_value -=50
        print("ah...I got shot...")

    def buy_gun(self,gun_name):
        print("%s just bought %s"%(self.name ,gun_name))



r1 = Role('Alex','police','AK47')#实例化 一个对象 初始化一个类
r2 = Role('JH','terrorist','B22')#Role这个类的实例

print(r1.name)
r1.show_status()
r1.got_shot()
r1.show_status()
#r1.__shot()
#
# '''
# r3 =Role('YZ','police','AK47')
# r3.got_shot()
# print(Role)
# r1.bullet_prove =True
# #新加的属性 是个性化的属性 与其他无关
# r3.buy_gun("b51")
# r1.buy_gun("AK47")
# Role.globle_resu['plice'].append(0)
# print(Role.globle_resu['plice'])
# '''
# r1.n_list.append("r1")
# r2.n_list.append("r2")
#
# print(r1.n_list)
#
# print(Role.n_list)