"""
        数组

"""
"""
        案例二百四十九 实例化数组

"""
print(f'{"案例二百四十九 实例化数组" :^30s}' + "\n")
# 数组实例化时需制定元素的类型,实例化后元素是可修改的
from array import array
import code
array1 = array('f',[0.001,0.002,0.003,0.004])
array2 = array('u',['上','下','左','右'])
array3 = array('i',(1,2,3,4))
print(f' array1: {array1}')
print(f' array2: {array2}')
print(f' array3: {array3}')
print("="*36)
"""
        案例二百五十 修改数组中的元素

"""
print(f'{"案例二百五十一 修改数组中的元素" :^30s}' + "\n")
# append():添加新元素到数组末尾 insert():插入新元素到指定位置
# 以from开头方法: 从其他对象提取新元素添加到数组的末尾
# remove(): 删除数组指定元素,若元素重复,则删除第一次出现的
# extend(): 一次性添加多个元素
array1 = array('u')
array1.append('正')
array1.extend('是江南好风景')
array1.fromunicode(' 落花时节又逢君')
print(f' array1: {array1}')
array2 = array('i')
array2.fromlist([1,2,3])
array2.insert(0,99)
array2.insert(1,88)
print(f' array2: {array2}')
print("="*36)
"""
        案例二百五十一 将数组内容存入文件

"""
print(f'{"案例二百五十一 将数组内容存入文件" :^30s}' + "\n")
file_name = 'mydata'
array1 = array('d')
array1.extend([10.001,9.009,8.008])
with open(file_name,mode='wb') as file:
        array1.tofile(file)
array2 = array('d')
with open(file_name,mode='rb') as file:
        try:
                array2.fromfile(file,3)
        except EOFError:
                pass
print(f' array2: {array2}')
print("="*36)