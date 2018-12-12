# -*- coding:utf-8 -*-
# Author: Jorden Hai

class School(object):

    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print("为学员%s办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣新员工%s并为其办理注册手续" % staff_obj.name)
        self.staffs.append(staff_obj)

class SchoolmStaff(object):

    members = 0  # 初始化人数

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):#需要实现的方法
        pass

class Teacher(SchoolmStaff):

    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of Teacher: ---- 
        Name:%s
        Age :%s
        Sex :%s
        Salary:%s
        Course:%s
        '''%(self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course:%s"%(self.name,self.course))

    # def __repr__(self):
    #     print("teacher")

class Student(SchoolmStaff):

    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ---- info of Student ---- 
        Name:%s
        Age :%s
        Sex :%s
        stu_id:%s
        grade :%s
        '''%(self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tuition for $ %s"%(self.name,amount))

xinhua_school = School("xinhua","Beijing")

t1 = Teacher("Oldboy",56,"MF",2000000,"Linux")

t2 = Teacher("Alex",22,"M",200000,"PythonDevOps")

s1 = Student("chenzhonghua",22,"M",1001,'PythonDevOps')

s2 = Student("xuliangwei",19,"M",1002,'Linux')

t1.tell()
s1.tell()
s2.tell()

xinhua_school.enroll(s1)
xinhua_school.enroll(s2)

xinhua_school.hire(t1)
print(xinhua_school.students)
print(xinhua_school.staffs)
xinhua_school.staffs[0].teach()

for stu in xinhua_school.students:
    stu.pay_tuition(10000)