"""
        多线程

"""

"""
        案例二百六十四 创建并启动新线程

"""
print(f'{"案例二百六十四 创建并启动新线程" :^30s}' + "\n")
from os import name
import threading
from time import sleep
from threading import Thread,current_thread
def do_work():
        th_name = current_thread().name
        print(f' 开始执行{th_name}线程')
        sleep(3)
        print(f' 线程{th_name}执行完毕')
th1 = Thread(target=do_work,name='thread_1')
th2 = Thread(target=do_work,name='thread_2')
th3 = Thread(target=do_work,name='thread_3')
th1.start()
th2.start()
th3.start()
print("="*36)
"""
        案例二百六十五 使用线程锁

"""
print(f'{"案例二百六十五 使用线程锁" :^30s}' + "\n")
# 为了保证数据同步,同一个资源在同一个时刻只允许一个线程访问.
from threading import Lock
num = 10
lock = Lock()
def work():
        global num
        while lock.acquire():
                if num > 0:
                        sleep(0.2)
                        num-=1
                        print(f' num: {num}')
                lock.release()
                if num == 0:
                        break
threads = [Thread(target=work) for i in range(5)]
for t in threads:
        t.start()
# 上下文管理器
with lock:
        if num > 0:
                sleep(0.2)
                num-=1
                print(f' num: {num}')
print("="*36)
"""
        案例二百六十六 等待事件信号

"""
print(f'{"案例二百六十六 等待事件信号" :^30s}' + "\n")
from threading import Event
evt_down1 = Event()
evt_down2 = Event()
def download_part1():
        print(' 正在下载 package1',end='')
        for i in range(8):
                sleep(0.5)
                print('#',end='')
        print('下载完成')
        # 下载完成,发送信息
        evt_down1.set()
def download_part2():
        # 等待第一个安装包下载完成
        evt_down1.wait()
        print(' 正在下载 package2',end='')
        for i in range(8):
                sleep(0.5)
                print('#',end='')
        print('下载完成')
        # 下载完成,发送信号
        evt_down2.set()
def install():
        # 等待第二个安装包下载完成
        evt_down2.wait()
        print(' 正在安装,请稍后......')
        sleep(2.5)
        print(' 安装完成')
th1 = Thread(target=download_part1)
th2 = Thread(target=download_part2)
th3 = Thread(target=install)
th1.start()
th2.start()
th3.start()
print('\n')
print("="*36)
"""
        案例二百六十七 屏 障

"""
print(f'{"案例二百六十七 屏 障" :^30s}' + "\n")
# 屏障(Barrier)在多线程同步中设置一道”栅栏“,当等待的线程数达到屏障对象所期望的数值时才会放行
# 若处于等待状态的线程数量未达到屏障所要求的值,所有线程会一直处于等待状态
import threading
br = threading.Barrier(parties=3)
def do_someThing():
        thname = threading.current_thread().name
        print(f' 线程{thname}已到达屏障')
        br.wait()
        print(f' 线程{thname}已通过屏障')
for i in range(3):
        t = threading.Thread(target=do_someThing,name=f'线程{i+1}')
        t.start()
print('\n')
print("="*36)