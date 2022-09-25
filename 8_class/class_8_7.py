"""
        上下文管理

"""

"""
        案例二百二十三 with语句

"""
print(f'{"案例二百二十三 with语句" :^30s}' + "\n")

with open('lines.txt',mode='wt',encoding='UTF-8') as file:
    file.write(' 今天是星期二\n')
    file.write(' 明天星期三\n')
print(f' 文件{"已" if file.close else "未"}关闭')

print("="*36)

"""
        案例二百二十四 自定义的类型支持上下文管理

"""
print(f'{"案例二百二十四 自定义的类型支持上下文管理" :^30s}' + "\n")

class demo1:
        def __enter__(self):
                print('=== 进入上下文 ===')
        def __exit__(self,*excinfo):
                print('=== 退出上下文 ===')
with demo1():
        print('   执行上下文代码   ')

class worker():
        def create(self):
                print(' 创建资源')
        def release(self):
                print(' 释放资源')
        def access(self):
                print(' 使用资源')
class demo2:
        def __init__(self) -> None:
            self.worker = worker()
        def __enter__(self):
                self.worker.create()
                return self.worker
        def __exit__(self,*exc_info):
                self.worker.release()
                if exc_info[0] is None:
                        return False
                else:
                        ex = exc_info[1]
                        print(f' 发生异常: {ex}')
                        return True
with demo2() as var:
        var.access()
        raise RuntimeError(' 普通错误')

print("="*36)

"""
        案例二百二十五 contextmanager 装饰器

"""
print(f'{"案例二百二十五 contextmanager 装饰器" :^30s}' + "\n")
from contextlib import contextmanager
class my_resource:
        def create(self,*nums,max_limit):
                print(' 正在初始化资源......')
                self.number = nums
                self.max = max_limit
                print(' 资源初始化完成')
        def release(self):
                del self.number
                self.max = 0
                print(' 资源已释放')
        def use(self):
                result = sum(self.number)
                if result > self.max:
                        raise Exception(f' 数值总和不能超过: {self.max}')

@contextmanager
def get_res(*args,max=5):
        res = my_resource()
        # 初始化资源
        res.create(*args,max_limit=max)
        try:
                yield res
        except Exception as exc:
                print(f' 发生异常: {exc}')
        finally:
                # 释放资源
                res.release()

with get_res(1,1,5,max=9) as r:
        # 使用资源
        a = r.use()
        print(f' 运行结果: {a}')

print('  ------------  ')

with get_res(2,6,2,max=9) as r:
        # 使用资源
        a = r.use()
        print(f' 运行结果: {a}')

print("="*36)

"""
        案例二百二十六 使用closing类释放上下文资源

"""
print(f'{"案例二百二十六 使用closing类释放上下文资源" :^30s}' + "\n")

class test_res:
        @classmethod
        def create(cls):
                print(' 初始化资源')
                return cls()
        def doSomething(self):
                print(' 访问资源')
        def close(self):
                print(' 释放资源')
from contextlib import closing
with closing(test_res.create()) as res:
        res.doSomething()
print('   ------------   ')
with closing(open('lines.txt',mode='wt',encoding='UTF-8')) as f:
        f.write(' 测试文件输入')
print("="*36)