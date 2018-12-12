'''
f = open("txws_test.txt",'r',encoding='utf-8')
'''

'''
def find_start_imooc(f_name):
    f1 = open(f_name,'r',encoding='utf-8')
    for line in f1:
        if line.startswith("iMOOC"):
            print(line)

def find_end_imooc(f_name):
    f2 = open(f_name,"r",encoding="utf-8")
    for line in f2:
        if line.endswith("imooc"):
            print(line)

'''
#
# def find_in_Equipment(f_name):
#     f = open(f_name,'r',encoding="utf-8")
#     for line in f:
#         if line.startswith('【') and line[:-1].endswith('】'):
#             print(line)
#
#
# find_in_Equipment('txws_test.txt')
#
# find_in_Equipment('test.txt')
ss = 'imooc python'
import re
# 尽量使用元字符串
pa = re.compile(r'imooc')
pa.match(ss)
