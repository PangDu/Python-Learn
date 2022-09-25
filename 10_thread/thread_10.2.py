"""
        异步等待

"""

"""
        案例二百六十八 定义异步函数

"""
print(f'{"案例二百六十八 定义异步函数" :^30s}' + "\n")
async def runer1():
        print(f' runer1')
async def runer2():
    await runer1()
async def runer3():
    await runer2()
print("="*36)
"""
        案例二百六十九 执行异步函数

"""
print(f'{"案例二百六十九 执行异步函数" :^30s}' + "\n")
import asyncio
from time import sleep
async def asynPrint(max):
    for n in range(1,max+1):
        await asyncio.sleep(3)
        print(n,end=' ')
asyncio.run(asynPrint(6))
print('\n')
print("="*36)
"""
        案例二百七十 实例化Task对象

"""
print(f'{"案例二百七十 实例化Task对象" :^30s}' + "\n")
# asyncio.Task()  asyncio.create_task()
async def asyncFun():
    for n in range(1,6):
        await asyncio.sleep(1)
        print(f' 第{n}行文本')
async def main():
    myTask = asyncio.create_task(asyncFun())
    await myTask
asyncio.run(main())
print("="*36)