# -*- coding:utf-8 -*-
# Author: Jorden Hai

name = 'my \tname is alex'
name1 = 'my name is {name1}'
num = 1234
name = name.capitalize()
print(name)
print(name.count('A'))#区分大小写
print(name.center(50,'-'))
print(name.encode())
print(name.endswith('ex'))#以什么截止
print(name.expandtabs(tabsize=30))
print(name.find('name'))#字符串切片
print(name[name.find('name'):9])
print(name1.format(name1 = 'jh'))
print(name1.format_map({'name1':'alex'}))
print(name.isalnum())#是个阿拉伯数字
print('1234ascd'.isalnum())
print('abscc'.isalpha())#是否英文字符
print('a1a'.isdigit())#s是否整数
print('a21'.isidentifier())#是否是一个合法的标识符
print('121'.isnumeric())
print('121.11'.isnumeric())#仅为数字
print('a00 '.isspace())
print('My Name Is '.istitle())#tty dile 、drive file
print('My name Is '.isprintable())
print('My '.isupper())
print('My name is  '.join("=="))
print('+'.join(['1','2','3','4']))
print(name.ljust(50,'*'))
print(name.rjust(50,'-'))
print(name.lower())
print(name.upper())
print("       Alex".lstrip())
print("       Alex       \n".rstrip())
print("aaaa     ")
print("Alex    ".strip())

p = str.maketrans("abcdefhijkx","123456!@#$-")

print("alex li".translate(p))

print('alex li'.replace('l','L',1))
print('alex li l'.rfind('l')) #找到最后面那个值得坐标
print('alex li xiao huo zi '.split())
print('alex li xiao huo zi '.split('l'))
print('1+2+3+4'.split('+'))
print('1+2+3\n4+5+6'.splitlines())#按换行符
print('alex li'.startswith('l'))
print('alex li'.startswith('a'))
print('alex li'.endswith('i'))
print('alex li'.endswith('a'))

print('Alex Li'.swapcase())#烦
print('alex li'.title())

print('alex li'.zfill(20))

