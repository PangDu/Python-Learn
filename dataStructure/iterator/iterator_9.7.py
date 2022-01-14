"""
        迭代器

"""
"""
        案例二百五十六 iter函数与next函数

"""
print(f'{"案例二百五十六 iter函数与next函数" :^30s}' + "\n")
org_list = [1,2,3,4,5,6]
iterator = iter(org_list)
while True:
    try:
        x = next(iterator)
        print(f' x: {x}')
    except StopIteration:
        break
print("="*36)
"""
        案例二百五十七 yield语句与迭代生成器

"""
print(f'{"案例二百五十七 yield语句与迭代生成器" :^30s}' + "\n")
def make_nums():
    a = 2
    while a < 1000:
        a = yield a * 2
g = make_nums()
n = next(g)
while True:
    try:
        n = g.send(n)
        print(f' n: {n}')
    except StopIteration:
        break
print("="*36)
"""
        案例二百五十八 自定义迭代器

"""
print(f'{"案例二百五十八 自定义迭代器" :^30s}' + "\n")
class cust_iter:
        def __init__(self,max=5,step=1) -> None:
            self.max = max
            self.step = step
            self.vaule = 1
        def __iter__(self):
                return self
        def __next__(self):
                if self.vaule >= self.max:
                        raise StopIteration
                res = self.vaule
                self.vaule = self.vaule + self.step
                return res
it = cust_iter(max=10,step=2)
for n in it:
        print(f' n: {n}')
#while True:
#        try:
#                n = next(it)
#                print(f' n: {n}')
#        except StopIteration:
#                break
print("="*36)