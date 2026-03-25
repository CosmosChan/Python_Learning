#导入模块的方法
#1.import 模块名
#2.from 模块名 import 模块对象
#3.import 模块名 as 别名
import math as mt
print(mt.sqrt(9))
from math import sqrt
print(sqrt(9))

#常用的几个内置模块

#1.os模块:用来管理文件和目录的模块
import os
#方法名
#os.getcwd():返回当前的工作路径,current working directory
#os.chdir(路径名):指定自己的目录为当前的工作路径(cd)
#os.listdir(路径名):返回一个列表,列表内容为指定路径里的所有文件名和文件夹名
#os.mkdir(路径名):创建路径名中指定的列表
#os.方法名(指定列表)
#a = os.listdir('D:Python_Proj')#文件名列表
#print('列表内容:')
#print(a)
#os.chdir('D:\\Python_Proj')
#os.mkdir('test_2')#创建文件夹
#b = os.listdir('D:\\python_Proj')
#print('当前路径为:',os.getcwd())
#print('列表内容:')
#print(b)

#2.time模块:时间模块
#方法名:time.time()
#方法名:time.localtime()
#方法名:time.strftime(格式,元组时间),返回一个字符串格式,字符串格式化
import time
print(time.time())#返回当前时间,返回值为自纪元以来的秒数
print(time.localtime())#返回一个元组,包含年月日时分秒日期
#time.sleep(5)#休眠5秒,也就是停顿五秒
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#3.datetime模块
#方法名:datetime.date.today()返回当前日期
#方法名:datetime.datetime.today()返回当前日期时间
#方法名:datetime.datetime.now([时区])
import datetime
print(datetime.date.today())#只有日期
print(datetime.datetime.today())#日期加时间
print(datetime.datetime.now())#日期加时间


#4.random模块
#random.random()随机生成0-1之间的浮点数
#random.uniform(a,b)随机生成a-b之间的浮点数
#random.randint(a,b)随机生成a-b之间的整数
#random.choice(m)从m中随机获取一个元素
#random.sample(m,n)从m中随机获取n个元素,返回一个列表
import random
#print('%.3f'%random.random())
#print(random.uniform(1,10))
#print(random.randint(1,10))
#print(random.randint(1,10)+random.random())
#num_list = []
#for i in range(10):
#    num = random.randint(1,10) + random.random()
#    num_list.append(num)
#for i in range(len(num_list)):
#    print(num_list[i],'',end='')
#rand_choice = random.choice(num_list)
#print(rand_choice)

#随机生成四位字母与数字组合的验证码
#character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]
#verification_code = random.sample(character,4)
#print('四位验证码为',end = '')
#for i in range(len(verification_code)):
#    print(verification_code[i],end = '')
#print('\n')
#yanzhengma = ''#空字符串
#for i in range(4):
#    verify_code1 = str(random.randint(0,9))
#    verify_code2 = chr(random.randint(65,90))#chr接受一个0-255的整数值并返回一个对应的ASCII码
#    verify_code3 = chr(random.randint(97,122))
#    yanzhengma += random.choice([verify_code1,verify_code2,verify_code3])
#print('四位验证码为',yanzhengma)


#创建自己的模块
#import 文件名 :将编写好的任意一个.py文件当作一个模块导入其他.py文件中

#from verification_code import verification_code_generate
#length = int(input('请输入验证码长度: '))
#print('%d位验证码为:%s'%(length,verification_code_generate(length)))


#numpy模块:用于快速处理任意维度的数组数据,一般只用于存放数值数据,不存放其它类型的数据
import numpy as np
#1.数组生成函数
#np.array(m): #将m转化成一个数组
#np.array(m.dtype): #将m转化成一个类型为dtype的数组
#arrange(a,b[,c]): 生成一个从a开始到b结束(不包含b)且步长为c的一维数组,a省略时默认为0,c省略时默认为1,b无法省略
#linspace(a,b,n): 生成包含n个元素的等差数列,从a开始到b结束,(包含b)
#ones((n,m)): 返回指定维数的全1数组,参数为一个元组
#zeros((n,m))
#eye(n): 创建单位对角矩阵
#empty(n)或empty((n,m)): 创建一个空数组,只分配内存空间,不填充任何值


#一般创建一个数组可以先创建一个列表,通过转换符号进行生成数组
a = np.array([1,2,3,4,5])
print(a,type(a))
b = np.array([1,2,3,4,5],dtype = np.float32)
print(b,type(b))
c = np.arange(1,10,2)
print(c,type(c))
list = []
for i in [1,2,3,4,5]:
    list.append(i)
print(list,type(list))
new_arr = np.array(list)
print(new_arr,type(new_arr))
