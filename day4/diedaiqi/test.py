#-*- coding:utf-8 -*-


# print(all([1,-1,5]))
# print(any([1,-1,5]))
# a = ascii(['1','2'])
# print(type(a),[a])
#
# def syshi():pass
# print( callable(syshi))
# a = bytes("abcdef",encoding="utf-8")
# b = a.capitalize()
# # 字符串不可以修改
# # 字节也不可以
# print(b,a)
# a = bytearray("abcdef",encoding="utf-8")
# # a.capitalize()
# print(a[0])
# a[1] = 49
# print(a)
#
# c = chr(98)
# print(c)
# c = ord('c')
# print(c)

# 动态导入
# py_obj = compile(code = 'for i in range(10): print(i)','err.log','exec')
#
# delattr()
# 匿名函数

# def sayhi():
#     print('hi')
#     pass
#
# print((lambda n:print(n))(3))
# 过滤数据
# res = filter(lambda n:n>5,range(10))
# for i in res:
#     print(i)

# res = map(lambda n:n**2,range(10))
# for i in res:
# #     print(i)
#
# import functools
# # reduce jiang shangyige zhi de jieguo fugei xiayige zhi
# res = functools.reduce(lambda x,y:x+y,range(1,5))
# print(res)


# f,g = divmod(5,2)
# print(f,g)

class node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        #初始化链表为空表
        self.root = None
        self.nodeLayer = dict()

    # 根据输入的BFS的数据生成二叉树
    def initBinaryTree(self, *data):
        if data == None:
            raise ValueError('root node need one number')
        #  层数，从0开始
        layerCount = 0
        length = len(data)
        # 补为偶数
        if length%2 != 0:
            list(data).append('#')
            length += 1

        while self.power(2,layerCount) < length+1:
            self.nodeLayer[str(layerCount)] = list()

            start = self.power(2,layerCount)-1
            stop = min(start*2+1,length)

            if layerCount == 0:
                self.nodeLayer[str(layerCount)].append(node(data[0]))
                self.root = self.nodeLayer[str(layerCount)][0]
            else:
                nodeCount = 0
                for p,q in zip(range(start,stop,2),range(start+1,stop,2)):

                    self.nodeLayer[str(layerCount)].append(node(data[p]))
                    self.nodeLayer[str(layerCount)].append(node(data[q]))
                    # 上层节点
                    tmpNode = self.nodeLayer[str(layerCount-1)][nodeCount]
                    tmpNode.left = self.nodeLayer[str(layerCount)][p-self.power(2,layerCount)+1]
                    tmpNode.right = self.nodeLayer[str(layerCount)][q-self.power(2,layerCount)+1]

                    nodeCount += 1

            layerCount += 1

    def power(self, x, n):
        s = 1
        while n > 0:
            n = n - 1
            s = s * x
        return s

DLR_list = []
def DLR(node):
    DLR_list.append(node.val)
    if node.left  != None:
        DLR(node.left)
    if node.right != None:
        DLR(node.right)
    return DLR_list

tree = BinaryTree()
data = [1,\
        'G','A',\
        'H','B','H','B',\
        'O','C','O','C','O','C','O','C',\
        'P','D','P','D','P','D','P','D',\
        'P','D','P','D','P','D','P','D',\
        'M','E','M','E','M','E','M','E',\
        'M','E','M','E','M','E','M','E',\
        'M','E','M','E','M','E','M','E',\
        'M','E','M','E','M','E','M','E']
tree.initBinaryTree(*data)
print(DLR(tree.root))