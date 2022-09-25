"""
        向函数传递参数的方式

"""

"""
        案例一百五十二 按位置传递参数与按关键字传递参数

"""
print(f'{"案例一百五十二 按位置传递参数与按关键字传递参数" :^30s}' + "\n")

def combine(p1,p2,p3):
    return '_'.join((p1,p2,p3))
s1 = combine('ab','ca','ef')
s2 = combine('xyz','123','stx')
s3 = combine(p1='opq',p2='lmn',p3='uvw')
s4 = combine(p1='@',p2='#',p3='%')
s5 = combine('qwe','uio',p3='kjl')
s6 = combine('vbn',p2='dfg',p3='ddd')
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

print("="*36)

"""
        案例一百五十三 只能按关键字传递的参数

"""
print(f'{"案例一百五十三 只能按关键字传递的参数" :^30s}' + "\n")

def run_fun(p,args,*,mode=0):
    print(' 函数被调用')
    print(' 参数列表:')
    print(f' p = {p}, args = {args}, mode = {mode}')

run_fun('myApp','--x',mode=8)
run_fun('hello','world')

print("="*36)

"""
        案例一百五十四 只能按位置传递的参数

"""
print(f'{"案例一百五十四 只能按位置传递的参数" :^30s}' + "\n")
print('此种参数定义方法只能在内置函数中使用!\n')
a = abs(-2)
print(a)
#不能使用关键字传参: TypeError
#b = abs(x = 100)
#print(b)

print("="*36)
