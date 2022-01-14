"""
        与属性访问有关的函数

"""

"""
        案例一百七十 获取与设置属性

"""
print(f'{"案例一百七十 获取与设置属性" :^30s}' + "\n")

class demo_1:
    pass
a = demo_1()
setattr(a,'name','lin')
setattr(a,'age',18)
setattr(a,'number',9999)
v1 = getattr(a,'name')
v2 = getattr(a,'age')
print(f' name 属性值: {v1}, age 属性值: {v2}')

print("="*36)


"""
        案例一百七十一 检查属性是否存在

"""
print(f'{"案例一百七十一 检查属性是否存在" :^30s}' + "\n")

if hasattr(a,'age'):
    print(f' age = {a.age}')
else:
    print('不存在此属性!')

print("="*36)

"""
        案例一百七十二 delattr()函数

"""
print(f'{"案例一百七十二 delattr()函数" :^30s}' + "\n")

print(f' 删除前对象属性: {a.__dict__}')
delattr(a,'number')
print(f' 删除后对象属性: {a.__dict__}')

print("="*36)

"""
        案例一百七十三 vars()函数

"""
print(f'{"案例一百七十三 vars()函数" :^30s}' + "\n")

dict_ = vars(a)
print(f' 对象属性列表: {dict_}')

print("="*36)