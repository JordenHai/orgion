# -*- coding:utf-8 -*-
# Author: Jorden Hai
info = {
    'stu1101':"TengLan Wu",
    'stu1102':"LongZe Luola",
    'stu1103':"XiaoZe Maliya",
}
info['stu1101'] = "武藤兰"
info['stu1102'] = "泷泽萝拉"
info['stu1103'] = "小泽玛利亚"
info['stu1104'] = "苍井空"


for key,value in info.items():
    print(key,':',value)


print(info.get('stu1105'))
print('stu1103' in info)#info.has_key(1103) in py2.x


'''
del info['stu1101']
info.pop("stu1102")
'''
for v in info.values():
    print(v)


