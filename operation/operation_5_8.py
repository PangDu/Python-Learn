"""
        ------ 日期与时间 ------

"""

"""
        案例一百四十五 日期之间的比较

"""
print(f'{"案例一百四十五 日期之间的比较" :^30s}' + "\n")

import datetime
d1 = datetime.date(year=2009,month=12,day=10)
d2 = datetime.date(year=2012,month=10,day=3)
print(f' {d1} 比 {d2}小吗?\n{" 是的" if d1 < d2 else " 不是"}')

d1 = datetime.date(year=2017,month=5,day=1)
d2 = datetime.date(year=2017,month=4,day=15)
print(f' {d1} 比 {d2} 大吗?\n {"是的" if d1 > d2 else " 不是"}')

print("="*36)

"""
        案例一百四十六 计算时间差

"""
print(f'{"案例一百四十六 计算时间差" :^30s}' + "\n")

d1 = datetime.date(year=2012,month=3,day=16)
d2 = datetime.date(year=2014,month=3,day=16)
dlt_day = d2 - d1
print(f' 从{d1}到{d2}相距{dlt_day.days}天')

d1 = datetime.datetime(year=2019,month=1,day=1,hour=15,minute=30,second=0)
d2 = datetime.datetime(year=2019,month=1,day=1,hour=18,minute=45,second=0)
delt_m = d2 - d1
print(f' 从{d1.time()} 到 {d2.time()} 共有{delt_m.seconds}秒')

print("="*36)

"""
        案例一百四十七 timedelta类的乘法运算

"""
print(f'{"案例一百四十七 timedelta类的乘法运算" :^30s}' + "\n")

tlt = datetime.timedelta(minutes=30)
print(f' {tlt}除以2之后: {tlt/2}')
print(f' {tlt}乘以3之后: {tlt * 3}')

print("="*36)