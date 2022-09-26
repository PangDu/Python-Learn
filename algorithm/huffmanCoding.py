"""
    哈夫曼树:
    一个根节点及其左孩子节点和右孩子节点为一组,在根节点中不存放数据值,
    所有的值存放在左孩子节点且该树的右子树中除终端节点外,所有节点不存值.
"""
"""
    哈夫曼树首先设计两个分支,该分支按照二进制设计,左分支为0,右分支为1,
    依次按使用的频率进行排序,使用最多的数据作为根节点的左子节点,除了终端
    节点以外的右子树的节点均为空节点
"""
# 节点定义
from tkinter import YES

class HTNode(object):
    def __init__(self,left,right=None) -> None:
        self.left = left
        # 一般右节点为空
        self.right = right
# 哈夫曼树的定义
class HuffmanTree(object):
    def __init__(self) -> None:
        self.root = None
        #编码表
        self.code = {}
    # 数据排序
    def sort_data(self,input_str):
        # 统计输入的字符与次数
        list = []
        # 去重
        s_input = set(input_str)
        for i in s_input:
            list.append((i,input_str.count(i)))
        list.sort(key=lambda t:(t[1]),reverse=True)
        print('排序后的顺序是:',list)
        return list
    # 创建方法
    def create(self,input_str):
        # 排序
        list = self.sort_data(input_str)
        curNode = None
        # 右子树的层数
        code = '0'
        # 创建哈夫曼树
        for i in list:
            if self.root == None:
                self.root = HTNode(i[0])
                # 推入编码表,合并字典
                self.code.update({i[0] : code})
                code = '1'
                curNode = self.root
            else:
                # 判断是否是最后两个元素，若是将最后一个元素放入右节点中
                if list.index(i) + 2 == len(list):
                    curNode.right = HTNode(i[0],list[-1][0])
                    # 推入编码表,合并字典
                    self.code.update({i[0]: code + '0'})
                    # 最终元素
                    self.code.update({list[-1][0] : code + '1'})
                    break
                else:
                    curNode.right = HTNode(i[0])
                    self.code.update({i[0] : code + '0'})
                    code = code + '1'
        print(self.code)
    # 输出 code 表
    def output_code(self,input_str):
        code = ''
        for i in input_str:
            code = code + self.code[i]
        print('最终编码:',code)
# 测试
input_str = input('输入需要编码的数据')
ht = HuffmanTree()
ht.create(input_str)
ht.output_code(input_str)
