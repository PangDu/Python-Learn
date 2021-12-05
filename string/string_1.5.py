import string
"""
    案例二十三 转换字母大小写

"""
print(f'{"转换字母大小写" :^30s}' + "\n")
print("abcde".upper())
print("ASDbvcxx".upper())
print("QWERFDS".lower())
print("ERFCacvf".lower())
print("一二三四五345".lower())
print("一二三四五345".upper())
print("QWERasdf".swapcase())
print("="*36)

"""
    案例二十四 用"0"填充字符串

"""
str = string.Template('用$what填充字符串')
newStr = str.safe_substitute(what = "\"0\"")
print(f'{newStr :^30s}'+ "\n")
print("2345".zfill(9))
print("-342132".zfill(9))
print("rty".zfill(9))
print("="*36)

"""
    案例二十五 对齐方式

"""
print(f'{"对齐方式" :^30s}' + "\n")
strLeft = "左对齐".ljust(25,'<')
print(strLeft)
strRight = "右对齐".rjust(25,'>')
print(strRight)
strCenter = "居中对齐".center(30,'#')
print(strCenter)
print("="*36)

"""
    案例二十六 查找子字符串

"""
print(f'{"查找子字符串" :^30s}' + "\n")
src_str = "人攀明月不可得,月行却与人相遇"
indexLeft = src_str.find('月')
indexRight = src_str.rfind('月')
print(f'原字符串:{src_str}')
print(f'从左向右查找,"月"字的位置为: {indexLeft}.')
print(f'从右向左查找,"月"字的位置为: {indexRight}.')
print("="*36)