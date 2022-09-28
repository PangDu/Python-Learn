"""
    折半查找采用了分而治之的思想,要求数据采用顺序存储结构并且数据是有序的
"""
# Python性能分析
import cProfile
# 生成随机目标
import random
# 向上取整
import math
from re import search

# 查询数据集
data = range(1,1000000)
def myFun():
    # 需要执行的全部代码
    count = 1000
    while count > 0:
        count -= 1
        target = random.randint(0,1000000)
        search(data,target)
# 递归方式折半查找
def search(list,target):
    num = math.ceil(len(list) / 2)
    if target == list[num - 1]:
        print("找到目标值!",target)
    elif target > list[num - 1]:
        search(list[num:len(list)],target)
    else:
        search(list[0:num],target)
#
cProfile.run('myFun()')
"""
    Hello
    1、字符串前缀集合: 从第一个字符开始直到最后一个(不包括最后一个字符)<H,He,Hel,Hell>
    2、字符串后缀集合: 从最后一个字符开始直到第一个(不包括第一个字符)<o,lo,llo,ello>
"""