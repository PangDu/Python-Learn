from cgitb import reset
from ctypes import sizeof
from logging import exception
import queue
#----------顺序表的实现----------
class SeqList(object):
    def __init__(self,max=10) -> None:
        self.max = max # 创建时元素个数默认为10
        self.num = 0
        # 在所有的数列中填充None
        self.data = [None] * self.max
    #获取某个元素的值
    def get_item(self,key):
        if 0<= key < self.num:
            return self.data[key]
        else:
            raise Exception('超出索引!')
#在末尾加入数据
    def append(self,value):
    # 当前列表已满
        if self.num == self.max:
            self.data[self.num] = value
            #超出最大长度，进行+1操作
            self.num += 1
            self.max += 10
        else:
            self.data[self.num] = value
            self.num +=1
    # 插入数据
    def insert(self,key,value):
    # 若key>=num则在尾部插入数据
        if key >= self.num:
            self.append(value)
        else:
            # 若列表已满扩容
            if self.num == self.max:
                self.max += 10
            # for循环从大到小步进为-1
            for i in range(self.num,key,-1):
                self.data[i] = self.data[i-1]
            # 直接更改key位置的值
            self.data[key] = value
            self.num += 1
    # 删除元素操作
    def pop(self,key=-1):
        if self.num <= 0:
            raise exception('列表已经为空!')
        elif key == -1:
            self.data[self.num -1] = None
            self.num -= 1
        else:
            for i in range(key,self.num-1):
                self.data[i] = self.data[i+1]
            self.data[self.num-1] = None
            self.num -= 1
print('='*30)
# 创建列表
listMode = SeqList()
# 打印当前列表中的值
print('初始化列表')
print(listMode.data)
# 添加元素
listMode.append(1)
listMode.append(2)
listMode.append(3)
# 打印当前列表中的值
print('添加数字元素后:')
print(listMode.data)
# 插入元素
listMode.insert(2,4)
# 打印当前列表中的值
print('插入元素后:')
print(listMode.data)
# 删除元素
listMode.pop(0)
# 打印当前列表中的值
print('删除元素后":')
print(listMode.data)
print('='*30)
#----------链表的实现----------
# 节点的定义
class Node(object):
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
# 链表的实现
class LinkList(object):
    def __init__(self) -> None:
        # 初始化头结点
        self.head = None
        # 存储当前访问的临时节点
        self.cur = None
    def get_item(self):
        if self.cur is None:
            print('当前链表为空!')
        else:
            print('******链表元素是:')
            while self.cur is not None:
                print(self.cur.data)
                self.cur = self.cur.next
            print('链表打印完毕!******')
        self.resetCur()
    # 获取多项式
    def get_xItem(self):
        if self.cur is None:
            print('当前链表为空!')
        else:
            print('多项式是:')
            str = ''
            while self.cur is not None:
                if self.cur.data[0] < 0:
                    str = str + '%dx^%d' % self.cur.data
                else:
                    if str == '':
                        str = '%dx^%d' % self.cur.data
                    else:
                        str = str + '+%dx^%d' % self.cur.data
                self.cur = self.cur.next
            print(str)
        self.resetCur()
    # 重置中间变量
    def resetCur(self):
        self.cur = self.head
    # 在末尾加入数据
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            self.cur = self.head
        else:
            while self.cur.next is not None:
                self.cur = self.cur.next
            else:
                self.cur.next = Node(value)
        self.resetCur()
    # 插入数据
    def insert(self,pos,value):
        for i in range(0,pos):
            if self.cur.next is not None:
                self.cur = self.cur.next
            else:
                # 超出边界,直接家后面
                break
        node = Node(value)
        # 如果不为空,首先将原节点地址存放在新节点的next中
        if self.cur.next is not None:
            node.next = self.cur.next
        self.cur.next = node
        del node
        self.resetCur()
    # 删除元素
    def remove(self,value):
        # 中间节点保存上一个节点的地址
        tnode = self.head
        while self.cur.next is not None:
            if self.cur.data == value:
                tnode.next = self.cur.next
                break
            tnode = self.cur
            self.cur = self.cur.next
        else:
            raise Exception('没有找到制定元素')
        self.resetCur()

# 创建链表并添加数据
linkListMode = LinkList()
linkListMode.append(1)
linkListMode.append(2)
linkListMode.append(3)
linkListMode.append(4)
linkListMode.append(5)
# 打印内容
linkListMode.get_item()
# 插入数据
print('--插入数据4--')
linkListMode.insert(2,4)
# 打印内容
linkListMode.get_item()
# 输出元素4
print('--删除元素4--')
linkListMode.remove(4)
linkListMode.get_item()
# 创建多项式
print('创建多项式')
linkListModes = LinkList()
linkListModes.append((2,3))
linkListModes.append((5,6))
linkListModes.append((-1,7))
linkListModes.append((2,8))
# 打印内容
linkListModes.get_xItem()
print('='*30)
# 栈的实现
lists = []
lists.append(1)
lists.append(2)
lists.append(3)
lists.append(4)
print(lists)
lists.pop()
lists.pop()
print(lists)
# 线性表实现栈的基本操作
class StackSeqList(object):
    def __init__(self,max=10):
        self.max = max
        self.num = 0
        self.top = -1
        self.data = [None] * self.max
        self.status = True
    # 入栈
    def append(self,value):
        if self.status:
            if self.num == self.max:
                self.data[self.num] = value
                self.num += 1
                self.max += 1
            else:
                self.data[self.num] = value
                self.num += 1
            # 更改栈顶数据索引位置
            self.top += 1
        else:
            a = self.pop()
            b = self.pop()
            self.status = True
            print('乘除法计算:' + str(b) + str(a) + value)
            if a == '*':
                self.append(int(b) * int(value))
            else:
                self.append(int(b) / int(value))
        # 判断符号是什么
        if value == '*' or value == '/':
            self.status = False
    # 出栈
    def pop(self):
        if self.num <= 0:
            raise Exception('栈已空！')
        res = self.data[self.top]
        self.data[self.top] = None
        self.num -= 1
        self.top -= 1
        return res
    def getRes(self):
        t1 = StackSeqList()
        res = 0
        t = ''
        while self.num > 0:
            t1.append(self.pop())
        while t1.num > 0:
            tc = t1.pop()
            if t == '':
                res = int(tc)
            else:
                if t == '-':
                    print('减法计算:' + str(res) + str(t) +str(tc))
                    res = res - int(tc)
                elif t == '+':
                    print('加法计算:' + str(res) +str(t) +str(tc))
                    res = res + int(tc)
            t = tc
        return res
# 顺序栈操作
stackList = StackSeqList()
print('初始化栈:')
print(stackList.data)
stackList.append('a')
stackList.append('b')
stackList.append('c')
stackList.append('d')
print('入栈后:')
print(stackList.data)
stackList.pop()
stackList.pop()
print('两次出栈后:')
print(stackList.data)
print('='*30)
# 四则运算
calculation = "3*6+9-8/2 "
l = StackSeqList()
for i in calculation:
    if i == ' ':
        print(l.getRes())
    else:
        l.append(i)
# 队列的实现
class QueueSeqList(object):
    def __init__(self,max=10) -> None:
        self.max = max
        self.num = 0
        self.data = [None] * self.max
    # 入队
    def append(self,value):
        if self.num == self.max:
            self.data[self.num] = value
            self.num += 1
            self.max += 1
        else:
            self.data[self.num] = value
            self.num +=1
    # 出队
    def pop(self):
        if self.num <= 0:
            raise Exception('队列已空！')
        for i in range(1,self.num):
            self.data[i - 1] = self.data[i]
        self.data[i] = None
        self.num -= 1
queueList = QueueSeqList()
print('初始化队列:')
print(queueList.data)
queueList.append(1)
queueList.append(2)
queueList.append(3)
queueList.append(4)
print('推入队列后:')
print(queueList.data)
queueList.pop()
queueList.pop()
print('出队:')
print(queueList.data)