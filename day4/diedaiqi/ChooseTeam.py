#-*- coding:utf-8 -*-

N = ['G','H','O','P','M']
M = ['A','B','C','D','E']
print(N)
print(M)
team_list = {'kqhw':[N[0],M[0]],\
             "dfhw":[N[1],M[1]],\
              'xqf':[N[2],M[2]],\
              "dqf":[N[3],M[3]],\
               "zf":[N[4],M[4]]}
team_num = [i for i in range(32)]
def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            while l.__len__() < 5:
                l.append(str(0))
            return ''.join(l[::-1])

for i in range(32):
    if i <= 15:
        team_num[i] = dec2bin(i)
    else:
        team_num[i] = dec2bin(i)

for i in range(32):
    l = team_num[i]
    print("这是第%d次名单"%(i+1))
    print('''
    控球后卫 得分后卫 小前锋 大前锋 中锋
       {kqhw}\t  {dfhw}\t\t {xqf}\t   {dqf}\t{zf}
    '''.format(kqhw=team_list['kqhw'][int(l[0:1])],\
               dfhw=team_list['dfhw'][int(l[1:2])],\
                xqf=team_list['xqf'][int(l[2:3])],\
                dqf=team_list['dqf'][int(l[3:4])],\
                 zf=team_list['zf'][int(l[4:5])]))


