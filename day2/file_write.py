
# f = open("yesterday2",'w',encoding='utf-8')
#
# f.write("我爱北京天安门,\n")
# f.write("天安门上太阳升.\n")
#
# f.close()


f = open("yesterday2",'a',encoding='utf-8')
# 如果什么都不写参数 会清空数据
# 从开头截断 移动光标是不好使的 兄弟
f.seek(10)
f.truncate(10)