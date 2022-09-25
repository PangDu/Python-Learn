"""
        字符界面

"""

"""
        打印久久乘法口诀

"""
for i in range(1,10):
    for j in range(1,i+1):
        print('{0} * {1} = {2}'.format(j,i, i *j),end=" ")
    print(' ')
print("="*36)

"""
        斐波那锲数列
"""
def fab(n):
    if n <=0:
        return '传递参数必须是大于零的正整数!'
    elif n ==1:
        return 0
    else:
        a,b = 0,1
        fab_list = [0,1]
        for i in range(n-2):
            a,b = b,a+b
            fab_list.append(b)
        return fab_list
print(fab(16))
print("="*36)
"""
        对文本进行分词
"""
#split()第一种用法
vstring = '人生苦短,我用Python!'
vret = vstring.split(',')
print(vret)
print(len(vret))
#split()第二种用法
import re
vstring = '人生苦短,我用Python!Python高效、优雅、很多人喜欢。ok'
vret = re.split('[,!、。]',vstring)
print(vret)
print(len(vret))
#sorted排序
dic = {'a':100,'b':90,'y':10,'t':200,'p':70}
vret = sorted(dic.items(),key=lambda item:item[0])
print(vret)
vret = sorted(dic.items(),key=lambda item:item[1])
print(vret)
#
def get_char(txt):
    vlist = re.split('[:;,."\s]\s*',txt)
    vdic_frequency=dict()
    for vchar in vlist:
        if vchar in vdic_frequency:
            vdic_frequency[vchar] += 1
        else:
            vdic_frequency[vchar] = 1
    vdic_sort = sorted(vdic_frequency.items(),key=lambda item:item[1],reverse=True)
    return vdic_sort
if __name__ == '__main__':
    with open('3.txt','r') as f:
        vtext = f.read()
    print(vtext)
    vstr = get_char(vtext)
    print('列出文本中的词语:\n')
    print(vstr)
print("="*36)