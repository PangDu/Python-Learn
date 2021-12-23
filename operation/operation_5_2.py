"""
        案例一百零六 Decimal类的简单使用

"""
print(f'{"案例一百零六 Decimal类的简单使用" :^30s}' + "\n")
import decimal
d1 = decimal.Decimal(0.00001)
d2 = decimal.Decimal('3.156')
d3 = decimal.Decimal(8888)
d4 = decimal.Decimal()
print(f' d1 : {d1}\n d2 : {d2}\n d3 : {d3}\n d4 : {d4}\n')
print("="*36)

"""
        案例一百零七 通过元祖对象初始化Decimal类

"""
print(f'{"案例一百零七 通过元祖对象初始化Decimal类" :^30s}' + "\n")
x1 = decimal.Decimal((0,(1,2,0,0,0,0,0,6),-5))
x2 = decimal.Decimal((1,(0,3,3),-2))
x3 = decimal.Decimal((0,(9,9,0),0))
print(f' x1 : {x1}\n x2 : {x2}\n x3 : {x3}\n')
print("="*36)

"""
        案例一百零八 通过DecimalTuple初始化Decimal类

"""
print(f'{"案例一百零八 通过DecimalTuple初始化Decimal类" :^30s}' + "\n")
tp = decimal.DecimalTuple(0,(2,5,7,2,5),-3)
dc = decimal.Decimal(tp)
print(f' dc : {dc}\n')
print("="*36)

"""
        案例一百零九 设置浮点数的精度

"""
print(f'{"案例一百零九 设置浮点数的精度" :^30s}' + "\n")
c = decimal.Context(prec= 4)
src = (0.005123456,43213.99,23.2438975,-20.09876)
for n in src:
    dx = c.create_decimal(n)
    print(f'{n :18f} >>> {dx}')
print("="*36)

"""
        案例一百一十 基于线程的浮点数环境

"""
print(f'{"案例一百一十 基于线程的浮点数环境" :^30s}' + "\n")
import threading
def theFun(prec):
    ctx = decimal.getcontext()
    ctx.prec = prec
    tname = threading.current_thread().name
    dx = ctx.create_decimal(150.8765489)
    print(f'线程:{tname},精度 : {prec}, 浮点数 :{dx}',end='\n')

th1 = threading.Thread(target=theFun,kwargs={'prec': 2},name= '线程 - 1')
th2 = threading.Thread(target=theFun,kwargs={'prec': 4},name= '线程 - 2')
th3 = threading.Thread(target=theFun,kwargs={'prec': 6},name= '线程 - 3')

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()
print("="*36)