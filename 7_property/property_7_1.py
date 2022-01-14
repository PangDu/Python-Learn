"""
        动态读写属性

"""

"""
        案例一百六十六 简单的属性访问

"""
print(f'{"案例一百六十六 简单的属性访问" :^30s}' + "\n")

class demo_1:
    pass
x = demo_1()
x.art_1 = 0.1
x.art_2 = 5
x.art_3 = 'hello'
print(f' art_1 : {x.art_1}, art_2 : {x.art_2}, art_3 : {x.art_3}')

try:
    print(f'art_4 : {x.art_4}')
except Exception as ex:
    print(f' 错误: {ex}')

print("="*36)

"""
        案例一百六十七 删除属性

"""
print(f'{"案例一百六十七 删除属性" :^30s}' + "\n")

class person:
    pass

p = person()
p.name = 'lin hei'
p.phoneNumber = 9999999

del p.phoneNumber
try:
    print(f' p.phoneNumber : {p.phoneNumber}')
except Exception as ex:
    print(f' 错误: {ex}')

print("="*36)

"""
        案例一百六十八 __dict__成员

"""
print(f'{"案例一百六十八 __dict__成员" :^30s}' + "\n")

class pet:
    pass
s = pet()
s.__dict__['name'] = 'lin'
s.__dict__['age'] = 18
s.__dict__['family'] = '宠物狗'
print(' name : {}, age : {}, family : {}'.format(s.name,s.age,s.family))
print(' __dict__成员:{}'.format(s.__dict__))

print("="*36)


"""
        案例一百六十九 区分类型属性与案例属性

"""
print(f'{"案例一百六十八 __dict__成员" :^30s}' + "\n")

class demo_2:
    pass

demo_2.prop1 = 100
demo_2.prop2 = 'hello'

x = demo_2()
x.value_1 = 'a'
x.value_2 = 99

print(f' 类属性: {demo_2.__dict__}')
print(f' 对象属性: {x.__dict__}')
print(f' x.prop1 : {x.prop1}, x.prop2 : {x.prop2}')

print("="*36)