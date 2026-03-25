import os
#类的定义:分为无参类和有参类
#类的大致结构为:
#class 类名:
#    属性函数(如果有此函数,则必须要有类似self这样的一个形参)
#    方法函数(如果有此函数,则必须要有类似self这样的一个形参)
#无参类
class Cjj:
    def Personal_Info(self):#self是必须有的一个形参,不管是对于属性函数还是方法函数而言,实参则是类的对象,像下面的chenjiajun
        print('姓名是'+self.name+',性别是'+self.sex+',身份证号是'+self.id)
chenjiajun = Cjj()
chenjiajun.name = '陈佳俊'
chenjiajun.sex = '男'
chenjiajun.id = '320803200508144211'
chenjiajun.Personal_Info()
class Person:
    def __init__(self,x,y,z):#Person的属性有身份证,姓名,性别等,这里加入三个形参x,y,z
        self.name = x
        self.sex = y
        self.id = z
    def Personal_Info(self):
        print('姓名是'+self.name+',性别是'+self.sex+',身份证号是'+self.id)
#如果像如下这么写则出现问题,有参数的类的定义必须要先传入参数才能定义,与无参类不一样
#cjj = Person()
#cjj.name = '陈佳俊'
#cjj.sex = '男'
#cjj.id = '320803200508144211'
#cjj.Personal_Info()
cjj = Person('陈佳俊','男','320803200508144211')
cjj.Personal_Info()
#但是怎样可以一开始不给参数呢?就像无参函数一样,默认没有值或者给定一个默认值则ok
class Person1:
    def __init__(self,x):
        self.name = x
        self.sex = '男'
        self.id = '320803200508144211'
    def Personal_Info(self):
        print('姓名是'+self.name+',性别是'+self.sex+',身份证号是'+self.id)
cjj = Person1('陈佳俊')
#此时我们后面再赋值,像str,list,dict等应该都是默认参数或者说是无参数的类
cjj.sex = '女'
cjj.id = '320803200508144210'
cjj.Personal_Info()
#或者如上这种定义时有默认值,在后续需要进行赋值的,可以额外定义一个方法函数
class Person2:
    def __init__(self,x):
        self.name = x
        self.sex = '男'
        self.id = '320803200508144211'
    def Personal_Info(self):
        print('姓名是'+self.name+',性别是'+self.sex+',身份证号是'+self.id)
    
    def setSex(self,x):
        self.sex = x
    def setId(self,x):
        self.id = x
cjj = Person2('陈佳俊')
cjj.setSex('女')
cjj.setId('320803200508144212')
cjj.Personal_Info()

#综上看来,类实际上只需要传入一个对象名形参self,后面的属性可以直接在语句里或者函数里通过self.属性名进行定义
#如果函数需要传入其他形参,可以设置默认值也可以进行在定义的一开始则要求赋值

#一个有意思的点,当没有确定如何写当前类的时候,可以先写一个空类,然后通过pass来空白占位预留而不报错
class Person3:
    pass

#类变量和实例变量
#可以申明很多个实例变量,其属性也是属于每个实例变量的一个副本,而类变量在全局主程序只有一个,通过类名或对象实例名均可以修改

#下面定义了一个类变量
class Car:
    price = 300000 #类变量,可以使用car1,car2,Car来访问和修改
    def __init__(self,name):
        self.name = name
        self.color = str()
    def setColor(self,color):
        self.color = color
    @ classmethod#类方法的定义
    def getPrice(cls):#类方法的第一个变量也不需要传入,类似于self
        print(cls.price)
    @ staticmethod
    def PrintInfo():
        print('这是一个宝马汽车')
car1 = Car('奥迪')
car2 = Car('宝马')
print(car1.name,Car.price) #打印实例变量和类变量的值
Car.price = 310000 #修改类变量的值
print(car2.name,Car.price)
car1.setColor('黑色')
car2.setColor('红色')
print(car1.name,car1.color,car1.price)


#类方法和实例方法
#实例方法的第一个参数为self
#类方法通过装饰器@ classmethod 来定义
#类方法通过类名来访问,也可以通过实例方法来访问
Car.getPrice()
#静态方法@ staticmethod
#静态方法既可以通过类变量来执行也可以通过实例变量来执行
Car.PrintInfo()
car1.PrintInfo()

#私有成员和公有成员
#_xxx,不能用'from module import *'来导入
#__xxx__,是系统定义的特殊成员
#__xxx,是类中的私有成员,只有类自己能访问,外部实例无法访问
#Python中可以通过定义私有变量并定义相应的访问该私有变量的方法,并使用@ property装饰器装饰这些函数
class Persons:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    @ property
    def getname(self):
        #"""I'm the  property"""
        return self.__name
cjj = Persons('cjj',18)
#print(cjj.__name)
print(cjj.getname)

#继承
#定义子类时,必须在括号内指定父亲的名称。子类创建实例时,不会自动调用父类的__init__()方法,因此
#需要子类调用父类的__init__()方法
class ECar(Car):#上面的Car类为父类
    def __init__(self,name):
        super().__init__(name)
        self.battery_size = 500
    def getEcar(self):
        print(self.name,'的电量为',self.battery_size)
my_tesla = ECar('特斯拉')
my_tesla.getEcar()