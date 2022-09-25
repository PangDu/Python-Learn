print(f'__init__:被访问')
def test_f1():
    print(f'{test_f1.__name__}被调用')

def test_f2():
    print(f'{test_f2.__name__}被调用')