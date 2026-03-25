import math

#函数定义
#def 函数名(参数列表):#参数列表可以没有,但圆括号必须要有
#    函数体
#    return 函数返回值


#1.无参函数
#def print_hello():
#    print('hello world')
#print_hello()
#
##2.有参函数
#def add2num(x,y):
#    return x+y
#
#print(add2num(15,32))
#
##3.可输入参数
#def add2num2(x,y):
#    c = x+y
#    return c
##x = int(input('请输入数字x:'))
##y = int(input('请输入数字y:'))
#total_num = input('请输入x,y两个数字(用空格隔开): ')
#x,y = total_num.split()
#print('两数相加结果为:',add2num2(int(x),int(y)))
#
##如果在同一个程序中出现了全局变量与局部变量同名的情况,那么在执行函数体内的语句时使用局部变量
#
#
##4.lambda表达式
##变量名 = lambda 参数列表: 表达式(一般是直接return的表达式)
##e.g.
#function = lambda x,y: x+y
#print(function(15,32))

#编写一个函数,求数列1,-2,3,-4,5,-6....,-100的和
#def sum(n):#n为长度
#    sum = 0
#    for i in range(n+1):
#        if i % 2 == 0:
#            sum += -i
#        else:
#            sum += i
#    return sum
#length = int(input('请输入数列的长度:'))
#print('该数列的和为:',sum(length))

#定义一个函数求解百钱百鸡的问题
def hun_money_hun_chicken():
    price_a = 5
    price_b = 3
    price_c = 1/3
    for i in range(101):
        for j in range(101):
            if i * price_a + j * price_b + (100 - i - j) * price_c == 100:
                print('公鸡有%d只,母鸡有%d只,小鸡有%d只'%(i,j,100-i-j))
hun_money_hun_chicken()


#求1-10的阶乘和:1+2!+3!+...+10!
def factorial(n):
    sum = 1
    i = n
    while i > 1:
        sum = i * sum + 1
        
        i = i - 1
    return sum
print('1-10的阶乘和为%d'%factorial(10))


#实训项目1
#2.(1)
#def function_1(x,y,z):
#    circle = int(4 * (x+y+z))
#    volumn = int(x*y*z)
#    #print(circle)
#    #print(volumn)
#    return [circle,volumn]
#s = input('请输入长宽高(以空格隔开):')
#x,y,z = s.split()
#print(function_1(int(x),int(y),int(z))[0],function_1(int(x),int(y),int(z))[1])

#2.(2)
#编写函数,计算1+1/2-1/3+1/4-1/5+1/6+...+(-1)^n/n
#def calculate_1(n):
#    sum = 1
#    for i in range(2,n+1):
#        if i % 2 == 0:
#            sum += 1/i
#        else:
#            sum += -1/i
#    return sum
#n = int(input('请输入n的值:'))
#print('最终的结果为:',calculate_1(n))

#2.(3)
#编写函数,从键盘输入一个数,判断是否为素数
#def function_2(x):
#    tag = 0
#    if x == 1 or x == 2:
#        print('不是素数')
#        return
#    for i in range(2,x):
#        if x % i == 0:
#            tag = 1
#            print('不是素数')
#            break
#    if tag == 0:
#        print('是素数')
#n = int(input('请输入一个正整数:'))
#function_2(n)

#2.(4)
#def calculate_2(n):
#    factor = []
#    if n == 1:
#        factor = 1
#        return
#    for i in range(1,n+1):
#        if n % i == 0:
#            factor.append(i)
#    return factor
#n = int(input('请输入一个正整数:'))
#factor = calculate_2(n)
#for i in range(len(factor)):
#    print(factor[i],'',end = '')

#2.(5)
#求最大公约数和最小公倍数
#def calculate_3(x,y):
#    GCD = 0
#    LCM = 0
#    for i in range(1,x*y+1):
#        if i % x == 0 and i % y == 0:
#            LCM = i
#            break
#    min_num = 0
#    if x > y:
#        min_num = y
#    else:
#        min_num = x
#    tag = min_num
#    while tag > 0:
#        if x % tag == 0 and y % tag == 0:
#            GCD = tag
#            break
#        tag -= 1
#    return [LCM,GCD]
#
#s = input('请输入两个正整数:')
#x,y = s.split()
#print('最小公倍数是: %d , 最大公约数是: %d'%(calculate_3(int(x),int(y))[0],calculate_3(int(x),int(y))[1]))


#2.(6)
#def function_4(n):
#    factor = []
#    if n == 1:
#        factor = 1
#        print('该数是完全数')
#        return
#    temp = 0
#    for i in range(1,n):
#        if n % i == 0:
#            temp += i
#    if temp == n:
#        print('该数是完全数')
#    else:
#        print('该数不是完全数')
#n = int(input('请输入一个正整数:'))
#function_4(n)

#参数类型
#位置参数,调用函数时按相应位置传入参数
#关键字函数,调用函数时按参数名传入函数
def dis(x1,y1,x2,y2):
    print('x1 = %d , y1 = %d , x2 = %d , y2 = %d'%(x1,y1,x2,y2))
    print(math.sqrt((x1-x2)**2 + (y1-y2)**2))
dis(x1 = 1 , y2 = 5 , y1 = 3 , x2 = 4)
#默认值参数
#不定长数目参数
#def function(a,*b),此处的*b表示可变参数，*b表示一个元组
def funct_1(a,*b):
    print(b)
    print(type(b))
funct_1(1,2,3,4,5,6)#其中2,3,4,5,6实参被打包成元组tuple传递给b
funct_1(1,2,3)
# *加在实参前面表示序列拆包
#相当于形参是元组,实参是实际的值,通过*来拆包
lst = [2,7,5]
print(lst)
print(*lst)
#两个**连在一起可以将参数收集到一个字典中,**加在字典前面表示字典拆包,可以用这种方式合并两个字典
#可以在传入参数的时候同时定义一个参数
d = ''
def funct_2(a = [] , b = {} , c = set() , d = ''):
    print(a[0],a[1])
    print(b['name'],b['age'])
    print(c)
    print(d)
funct_2([1,2,3,4,5] , {'name':'张三','age':18} , (1,2,3,4,5) , 'cjj')

#如果函数没有返回值,默认返回None,如果是return后没有返回值,函数的返回值也相当于None
#统计给定的整数M和N区间内的素数的个数,并对它们求和
#def calculate_5(m,n):
#    sum = 0
#    num = 0
#    list_number = []
#    for i in range(m,n+1):
#        tag = 0
#        for j in range(2,i):
#            if i % j == 0:
#                tag = 1
#        if tag == 0:
#            sum += i
#            num += 1
#            list_number.append(i)
#    return [num,sum,list_number]
#m = (int)(input('请输入左区间m的值:'))
#n = (int)(input('请输入右区间n的值:'))
#print('素数的个数是: %d , 素数的和是: %d , 素数是: %s'%(calculate_5(m,n)[0],calculate_5(m,n)[1],calculate_5(m,n)[2]))


def func1(x):
    return {'a':1000,'b':100}
print(func1('a'))


#内置sorted函数
students = [('将星',89,15),('小王',90,16),('小李',80,17)]
print(sorted(students,key = lambda x:x[1]))

#map()函数用法:map(function,iterable)
a = list(range(1,10))
#如果是进行类型转换,则直接用map(类型,iterable)
#如果是要进行表达式的每个元素进行映射,则需要使用lambda函数
b = map(str,a)
print(list(map(str,a)))  
print(list(map(float,a)))
print(sum(list(map(lambda x:x*x,a))))
#或者可以理解为lambda也是一个定义运算函数,对Iterable中的元素进行操作
