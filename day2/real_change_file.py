#修改必须加载到内存中
#或则
# 2013年的时候 我觉得我自己50万好多
# 到了现在了，我一个月50万我都觉得少了
# old boy 有点土
# 阶级需要我们用双手去创造
# 人生要选对方向
# 2010年运维总监 年薪60万 年终奖40万
# 我只是学了技术 改变不了人生
#
# vi 和 vim

# 硬盘读写模式决定了方法

f1 = open("yesterday2",'r',encoding='utf-8')
# 读模式
f2 = open("yesterday3","w",encoding='utf-8')

for line in f1:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等ALEX享受")
    f2.write(line)

f1.close()
f2.close()

# 你打开的文件不清空
# 不用关闭
#
#

with open("yesterday2","r",encoding="utf-8") as f ,\
     open("yesterday3",'w',encoding="utf-8") as f2:
    for line in f:
        print(line)

