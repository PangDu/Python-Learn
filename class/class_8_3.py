"""
        元类

"""

"""
        案例一百九十七 使用type类创建新类型

"""
print(f'{"案例一百九十七 使用type类创建新类型" :^30s}' + "\n")

def _run(self):
    print(f' self: {self}')

members = {
    'one' : 1,
    'two' : 2,
    'run' : _run
}
G = type('G',(),members)
v = G()
print(f' 对象类型: {v.__class__}')
print(f' 对象成员: {dir(v)}')
v.run()

print("="*36)

"""
        案例一百九十八 元类的实现过程

"""
print(f'{"案例一百九十八 元类的实现过程" :^30s}' + "\n")


print("="*36)