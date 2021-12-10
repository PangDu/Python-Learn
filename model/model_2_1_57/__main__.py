import test
from importlib import reload
while True:
    c = input('请输入"r"')
    if c.lower() !='r':
        break
    reload(test)
    print(f'number: {test.number}')