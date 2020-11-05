"""
猜数字游戏

import random
def game():
    person_num=0
    computer_num=random.randint(1,10)
    while True:
        person_num=int(input("请输入一个数字："))
        if person_num<computer_num:
            print("大一点")
        elif person_num>computer_num:
            print("小一点")
        else:
            print("猜对了！")
            break
game()
"""


"""
def func1(a,b,c,*,d):
    # print("这是一个函数")
     print("参数a：", a)
     print("参数b：", b)
     print("参数c：", c)
     print("参数d：",d)
func1(1,2,3,d=4)
"""
"""
# lambda 表达式
func2= lambda x:x*2
print(func2(1))

# 列表
list1=[]
list1.append(1)
list1.append(2)
list1.insert(0,8)
# list1.remove(1)
# list1.sort(reverse=True)
# list1.reverse()
print(list1)
"""
"""
list2=[]
for i in range(1,4):
    list2.append(i**2)
print(list2)
list3=[i**2 for i in range(1,4)]
print("列表推导式：",list3)
list4=[i**2 for i in range(1,4) if i!=1]
# for i in range(1,4):
#     if i!=1:
#         list4.append(i**2)
print(list4)
list5=[i*j for i in range(1,5) for j in range(1,4)]
# for i in range(1,4):
#     for j in range(1,4):
#         list5.append(i*j)
print(list5)
"""
"""

# 元组
a=[4,5,6]
b=["q","w","e"]
tuple1=(1,2,3,3,3,3,a,b)
# tuple1[4][0]="o"
print(tuple1)
print(tuple1.count(3))
print(tuple1.index(1))


# 集合
a={1,2,3,4,5}
b={1,2,6,7,8}
# print(type(a))
# print(type(b))
# print("并集：",a.union(b))
# print("交集:",a.intersection(b))
# print("差集:",a.difference(b))
c={'s', 'k', 'h', 'w', 'o', 'j', 'd','e','d'}
print(set(c))
"""
"""
# 字典
dict1={"a":1,"b":2}
dict2=dict(a=1,b=2)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.popitem())
# print(dict1)
a={ i:i*2 for i in range(1,5)}
print(a)
"""
"""
# 系统自带模块
from requests import *
import random
import sys
# print(sys.path)
import os
import re
import json
import time
# 第三方开源模块
import yaml

# 自定义模块
from baidu import *
# search2()
# game()
# print(dir())
import random
print(dir(random))
import sys
print(sys.path)

# 格式化输出
name="lily"
age=20
list1=[1,2,3,4]
dic1={'name':'tony','gender':'male'}
# print("my name is {0},my age is{1},{0}{1}".format(name,age))
# print("list is {},dic is{}".format(list1[1],dic1))
# print("we age:{},{}and{}".format(*list1))
# print("we name is:{name},my gender is: {gender}".format(**dic1))
print(f"my name is {name},my age is {age},my list is {list1[0]},my dic is {name}")
# 调用upper方法将名字变成大写字母
print(f"my name is {name.upper()}")
# lambda表达式，
print(f"result is {(lambda x:x+2)(2)}")
"""
"""
# 文件读取
# f=open('data.txt')
# print(f.readline(3))
# print(f.readline(3))
# print(f.readline(3))
# f.close()
# with语句块，可以将文件打开后，操作完成，会自动关闭文件
# 图片读取需要使用rb，读取二进制的格式
with open('data.txt') as f:
    while True:
        line=f.readlines()
        if line:
            print(line)
        else:
            break
    # print(f.readlines())
"""
"""
python错误与异常
系统自带异常方法
try:
    num1=int(input("请输入一个除数："))
    num2=int(input("请输入一个被除数："))
    print(num1/num2)
except ZeroDivisionError:
     print("被除数不能为0")
except ValueError:
    print("需要输入数值型整数")
 except:
    print("这是一个通用型错误")
finally:
    print("无论有没有异常，都执行")
抛出异常
x=10
if x>5:
    raise Exception("这是一场异常")

# 自定义异常方法
class myexception(Exception):
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
raise myexception("value1","value2")

# 类
class person:
    name="default"
    age=0
    gender="male"
    weight=0
    # 构造方法，在类实例化的时候被调用
    def __init__(self,name,age,gender,weight):
        self.name=name
        self.age=age
        self.gender=gender
        self.weight=weight
    @classmethod
    def eat(self):
        print('eating')
    @classmethod
    def play(self):
        print('playing')
    def jump(self):
        print('jump')
zs=person('zhangsan',20,'male',140)
print(f'张三的姓名是：{zs.name},年龄是：{zs.age},性别是：{zs.gender},体重是：{zs.weight}')
zs.eat()
zs.jump()
zs.play()
person.name='tom'
print(person.name)
person.play()

# 标准库
# OS模块
import os
# os.mkdir('testdir')
# os.removedirs('testdir')
# print(os.listdir('./'))
# print(os.getcwd())
# print(os.path.exists('b'))
# if not os.path.exists('b'):
#     os.mkdir('b')
# if not os.path.exists('b/test.txt'):
#     f=open('b/test.txt','w')
#     f.write('hello,os using')
#     f.close()
print(os.listdir('./'))
# os.remove('b/test.txt')
# os.rmdir('b')
# os.remove('data.txt')
# os.remove('baidu.py')
# os.remove('testjson.py')

# time模块
import time
# 时间格式转换
# print(time.localtime())
# a=time.localtime()
# print(time.strftime('%Y-%m-%d  %H:%M:%S', a))
# 获取2天前的时间
# now_time=time.time()
# two_days_ago =now_time-60*60*24*2
# time_tuple=time.localtime(two_days_ago)
# print(time.strftime('%Y-%m-%d  %H:%M:%S', time_tuple))
# 获取3天后的时间
now_time=time.time()
three_days_after =now_time+60*60*24*3
time_tuple=time.localtime(three_days_after)
print(f"三天后此刻的时间为：",{(time.strftime('%Y-%m-%d  %H:%M:%S', time_tuple))})

# urllib 模块
import urllib.request
response: object=urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())

# math 模块
import math

print(math.ceil(5.4))
print(math.floor(5.5))
print(math.sqrt(36))
"""
# python第三方库
import requests
# requests库
r=requests.get("http://www.baidu.com")
print(r.status_code)
print(r.encoding)











































