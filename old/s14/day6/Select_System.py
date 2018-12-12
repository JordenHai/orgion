# -*- coding:utf-8 -*-
# Author: Jorden Hai

class School(object):

    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.grades = []
        self.staffs = []
        self.courses = []

    def create_course(course_kind):
        self.courses.append(course_kind)


class Course(object):

    def __init__(self,type,price,time,addr):
        self.type = type
        self.price = price
        self.time = time
        self.addr = addr


class Schoolmember(object):
    pass

class Teacher(Schoolmember):
    pass

class Student(Schoolmember):
    pass

