"""
        自定义序列

"""
"""
        案例二百五十九 实现按索引访问的集合

"""
print(f'{"案例二百五十九 实现按索引访问的集合" :^30s}' + "\n")
# 实现三个协议可以实现: __getitem__() __setitem__() delitem__()
class cust_list:
    def __init__(self,iterable = None) -> None:
         self.inner_list = []
         if iterable is not None:
             it = iter(iterable)
             for i in it:
                 self.inner_list.append(i * 2)
    def __getitem__(self,index):
        return self.inner_list[index]
    def __setitem__(self,index,value):
        self.inner_list[index] = value * 2
    def __delitem__(self,index):
        del self.inner_list[index]
    def add(self,value):
        self.inner_list.append(value * 2)
    def __str__(self) -> str:
        t = []
        for x in self.inner_list:
            t.append(repr(x))
        return ','.join(t)
    def __repr__(self) -> str:
        s = '{0}{1}'.format(type(self)).__qualname__,repr(self.inner_list)
mylist = cust_list([2,6,8])
mylist.add(5)
mylist.add(7)
mylist.add(9)
print(f' 列表: {mylist}')
del mylist[0]
print(f' 列表: {mylist}')
mylist[3] = 999
print(f' 列表: {mylist}')
print("="*36)
"""
        案例二百六十 统计集合的长度

"""
print(f'{"案例二百六十 统计集合的长度" :^30s}' + "\n")
class AvailableSet:
    def __init__(self) -> None:
        self.ele_store = []
    def add(self,value):
        self.ele_store.append(value)
    def remove(self,value):
        self.ele_store.remove(value)
    def remove_at(self,index):
        del self.ele_store[index]
    def clear(self):
        self.ele_store.clear()
    # 支持迭代操作
    def __iter__(self):
        self.current_index = -1
        return self
    def __next__(self):
        self.current_index += 1
        if self.current_index >= len(self.ele_store):
            raise StopIteration
        return self.ele_store[self.current_index]
    # 自定义字符串表示形式
    def __str__(self) -> str:
        return str(self.ele_store)
    # 自定义长度计算
    def __len__(self):
        c = 0
        for i in self:
            if i is None:continue
            if i == 0:continue
            if i == '':continue
            c += 1
        return c
myset = AvailableSet()
myset.add(10)
myset.add(0.0009)
myset.add('abc')
myset.add('')
myset.add(8888)
n = len(myset)
print(f' 集合中有效元素个数: {n}')
for x in myset:
    print(f' {x!r}'.ljust(8),end='')
print('\n')
print("="*36)
"""
        案例二百六十一 字典对象的访问协议

"""
print(f'{"案例二百六十一 字典对象的访问协议" :^30s}' + "\n")
class TypeKeyDict:
    def __init__(self,keyType=int) -> None:
        self.keyType = keyType
        self.innerDict = {}
    def __len__(self):
        return len(self.innerDict)
    def __str__(self):
        return str(self.innerDict)
    def __getitem__(self,key):
        self.check_key_type(key.__class__)
        try:
            return self.innerDict[key]
        except KeyError:
            pass
    def __setitem__(self,key,vaule):
        self.check_key_type(key.__class__)
        self.innerDict[key] = vaule
    def __missing__(self,key):
        self.check_key_type(key.__class__)
        return None
    # 迭代器
    def __iter__(self):
        x = []
        for k,v in self.innerDict.items():
            x.append((k,v))
        return iter(tuple(x))
    def check_key_type(self,keyType):
        if self.keyType != keyType:
            raise TypeError
    def containsKey(self,key):
        keys = self.innerDict.keys()
        return key in keys
    def keys(self):
        keys = self.innerDict.keys()
        return tuple(keys)

myDic = TypeKeyDict(keyType=str)
myDic['key1'] = 9999
myDic['key2'] = 0.8888
myDic['key3'] = '6666'
print(f' 字典中{"存在" if myDic.containsKey("key4") else "不存在"}key4的键')
print(f' 字典中元素数量: {len(myDic)}')
print(f' 获取key5对应的值: {myDic["key5"]}')
for k,v in myDic:
    print(f' {k} : {v}')
print("="*36)