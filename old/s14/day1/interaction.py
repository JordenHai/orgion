# -*- coding:utf-8 -*-
# Author: Jorden Hai
Name = input("Name:")
Age = int(input("Age:"))
Job = input("Job:")
Salary = int(input("Salary:"))
#raw_input_2.x input_3.x
#input_2.x 输入什么格式是什么格式 input() 多余的语法

print('name','=',type(Name))
#格式化输出 方案一
info='''
---------info of Stuff ----------
Name:%s
Age:%d
Job:%s
Salary:%d
'''%(Name,Age,Job,Salary)
#格式化输出 方案二
info2 = '''
---------info of Stuff ----------
Name:{_Name}
Age:{_Age}
Job:{_Job}
Salary:{_Salary}
'''.format(_Name = Name,
           _Age = Age,
           _Job = Job,
           _Salary = Salary)
#格式化输出 方案三
info3 = '''
---------info of Stuff ----------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(Name,Age,Job,Salary)
print(info,info2,info3)