"""
        案例二百六十二 切片

"""
print(f'{"案例二百六十二 切片" :^30s}' + "\n")
# obj[<start>:<end>:<step>]
a = [1,2,3,4,5,6,7,8,9]
print(f' s1:{a[:4]}')
print(f' s2:{a[1:7:2]}')
print(f' s3:{a[:-2]}')
print("="*36)
"""
        案例二百六十三 in 与 not in 运算符

"""
print(f'{"案例二百六十三 in 与 not in 运算符" :^30s}' + "\n")
b = (1,2,3,4,5,6,7)
if 10 in b:
    print(f' 10在元祖中')
else:
    print(f' 10不在元祖中')
if 999 not in b:
    print(' 999不在元祖中')
else:
    print(' 999在元祖中')
print("="*36)