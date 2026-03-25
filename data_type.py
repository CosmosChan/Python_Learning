#Python中,用;来控制多行代码在同一行中,用\控制一行代码的换行


#整型int
x = 3
print(x)
print(type(x))#class 'int'
print(type('x'))#class 'str'
#常用type来检测数据类型


#浮点型float
y = 3.14
print(y)
print(type(y))


#布尔型bool
z1 = False
z2 = 1>2
print(z1)
print(z2)
print(type(z1))
print(type(z2))


#字符串类型str
a = 'duweihan'
b = "chenjiajun"
c = '''cjj love dwh'''#三种字符串定义符都可以
print(a,b,c)
print('\n')
print(type(a),type(b),'\n',type(c))
#特殊字符\n的用法：放在print函数中,将输出结果换行
#python中变量的命名通过赋值来命名

#给多个变量命名
x_1 , x_2 , x_3 = 1,2,3
y_1 , y_2 , y_3 = 'dwh' , x_1<x_2 , 1.05
print(x_1,x_2,x_3)
print(y_1,y_2,y_3)

#运算操作符
x_a = 2
x_b = 3
y_result1 = x_a ** x_b#求幂
y_result2 = x_b / x_a#除法(自动改变变量类型)
y_result3 = x_b % x_a#求余
y_result4 = x_b // x_a#整除
print(y_result1)
print(y_result2)
print(y_result3)
print(y_result4)

#逻辑运算符and or not:需要用在布尔型变量上
#and运算规则：如果作用在两个非布尔型变量上,如果第一个值为0,则返回0,否则返回第二个值
#or运算规则同理可类推
a = True
b = x_a > x_b
c = a and b
print(c)
print(not(c))#逻辑运算符也可操作在一个变量上
print(a ^ b)
print(not(a) ^ c)
print(a | b)
print(a & b)
print(0 | 3)
print(1 & 0)
print(1 and 2)


#成员运算符in(逻辑运算符):判断一个字符或字符串是否在另一个字符串中
a = 'dwh'
b = 'cjj'
c = 'dwh' in 'cjj'
d = 'dwh' in 'cjj love dwh'
print(a,b,c,d)

import math

x11 = pow(2,3)
x12 = abs(-3)
x13 = round(3.1415926,3)#截取小数点后三位并四舍五入
x14 = math.sqrt(0.16)
print(x11,x12,x13,x14)

#类型转换函数int(str) , float(int) , float(str) , str(int) , bool(int)
x21 = float('520.1314')
x22 = str(520)
x23 = int(3.14)
x24 = math.floor(3.14)
print(x21,x22,x23,x24)

#字符串函数：str.upper() , str.lower() , str.capitalize() , str.title() , str.strip() , str.split()
#len(str) , ljust(str,n) , rjust(str,n) , find(str,start,end)
#replace(old,new,count)

x31 = 'cjj love dwh'
x32 = x31.center(20)
result1 = x31.upper()
result2 = x31.lower()
result3 = x31.capitalize()
result4 = x31.title()
result5 = x31.strip()#空白符消除函数,将字符串左右两边的字符串消除
result6 = x31.split()#切片符,把字符串内每个用空白字符隔开的完整的字符串依次输出出来
result7 = x31.find('cjj')
result8 = len(x31)
result9 = x31.replace('cjj','dwh',0)
result10 = x31.replace('cjj','dwh',1)
print(result1,"\n",result2,"\n",result3,"\n",result4,"\n",result5,"\n",result6,"\n",result7,"\n",result8,"\n",result9,"\n",result10)
result11 = x31.ljust(20,'*')
result12 = x31.rjust(20,'*')
result13 = x31.center(20,'*')
result14 = x31.ljust(5,'*')
result15 = x31.rjust(5,'*')
result16 = x31.center(5,'*')
print(result11,"\n",result12,"\n",result13,"\n",result14,"\n",result15,"\n",result16)
result17 = x32.strip()
result18 = x32.lstrip()
result19 = x32.rstrip()
result20 = x32.split()
print(x32 , "\n",result17 , "\n",result18 , "\n",result19 , "\n",result20)