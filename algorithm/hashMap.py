import random
from re import I
import time
class HashMap(object):
    def __init__(self,max = 30) -> None:
        self.max = max
        self.top = -1
        self.status = True
        self.data = [None] * self.max
    @staticmethod
    def get_key(id):
        return id % 25
    # 存储数据
    def save(self,value,id=-1):
        if id > self.max:
            for i in range(self.max,id+1):
                self.data[i] = None
                self.max = id + 1
        if id == -1:
            id = self.get_key(value)
            self.save(value,id)
        else:
            if self.data[id] is not None:
                print("出现冲突!")
                self.save(value,id+1)
            else:
                print("存贮地址为:" + str(id))
                self.data[id] = value
    # 查询数据
    def find(self,value_id,id=0):
        if id == 0:
            id = self.get_key(value_id)
            return self.find(value_id,id)
        else:
            if value_id != self.data[id]['id']:
                print("查找失败,稍等......")
            else:
                return self.data[id]
# 测试
hashMaps = HashMap()
for i in range(1,30):
    hashMaps.save(i)
print(hashMaps.data)