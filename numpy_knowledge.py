import numpy as np
#numpy数组必须包含同一类型的数据
#从Python列表创建Numpy数组
    #创建一个空数组,空数组只能是一维的
x = np.empty(10)#大小为10的一维空数组
a = np.array(['1','2','3'])
print(a)
b = np.array([list(range(i,i+3)) for i in [1,2,3,4,5]])
print(b)
#从头创建Numpy数组
a = np.zeros(10,dtype = np.int_)#长度为10,数据类型为整型
b = np.ones((3,5),dtype = float)#规模为3x5,数据类型为浮点型
c = np.ones((3,4,5),dtype = int)#规模为3x4x5,3行4x5矩阵
print(a,'\n',b,'\n',c)
d = np.full((3,4),3.14)#np.full(规模,数据)是用什么数据给数组填满的
print(d)
e = np.arange(0,20,2)#线性序列数组

f = np.random.random((3,3))#0-1均匀分布的3x3数组
g = np.random.normal(0,1,(3,3))#3x3,均值为0,标准差为1
h = np.random.randint(0,10,(3,7))#3x7,0-10之间的随机整数
print(e,'\n',f,'\n',g,'\n',h)
    #创建单位矩阵
a = np.eye(3)#3x3的单位矩阵
b = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(a,'\n',b)

x1 = np.linspace(0,10,3)#线性等差数列,从0开始,到10结束,元素个数为3个,注意与np.arange()函数的区别,arange只能生成整数数组,linspace()可以生成实数数组
x2 = np.arange(0,np.pi,3)
print('x1',x1)
print('x2',x2)

rng = np.random.default_rng(seed = 1701)#设置随机数种子,相比于np.random更好
x1 = rng.integers(10,size = 6)#上限为10,下限默认为0,左开右闭
x2 = rng.integers(10,size = (3,4))
    #等效于之前写的x2 = np.random.randint(0,10,(3,4))
x3 = rng.integers(10,size = (3,4,5))
    #每个数组有四种属性,分别为shape,dtype,size,ndim,数组每个维度的大小,数组类型,数组总大小,数组维数,用数组变量名.属性名来获取
print(x3.dtype,x3.shape,x3.size,x3.ndim)

#数组索引和切片元素获取
    #数组元素获取和列表一样,获取i行j列元素为a[i,j],列表操作为a[i][j],有些不太一样
    #获取倒数的索引为a[-i]
    #一维数组获取切片为a[start:end:step],多维数组获取切片为a[start1:end1:step1,start2:end2:step2,start3:end3:step3...]
    #用一个冒号表示空切片a[:,:,start:end:step],在获取行时可以省略空切片,a[1,:] = a[1]
print(x3[::-1,2:-1,:2:-2])
print(x3[:,:,::-1])
    #注意,数组的切片是原数组的视图而非副本,改变数组切片也会改变原数组
    #数组的视图有用,在处理大数据的时候可以选择使用数组的视图,而不是对整个数组进行操作
x4 = x3[:2,:2,:2]
print(x4,'\n',x3)
x4[0,0,0] = 100
print(x4,'\n',x3)

#创建数组的副本
    #可以简单地通过.copy()创建副本
x2_copy = x2[:2,:2].copy()#如果修改副本,原数组不会改变

#数组的变形
a = np.arange(0,20,2).reshape(2,5)#一个常见的操作是将一维数组变为二维数组,注意前后数组大小一致
print(a)
    #这样可以使一维数组得到行向量或列向量
a = np.arange(0,20,2).reshape(10,1)
print(a)
    #或者也可以通过np.newaxis切片语法来实现
a = np.arange(0,20,2)[np.newaxis,:]#在索引位置增加一个新轴,不改变原数组的大小,使得ndim增加1,
                                    #因此在第1维填入np.newaxis使得列增加一维,成为二维列向量
b = np.arange(0,10,2)[:,np.newaxis]
print(a,'\n',b)

#数组的拼接和拆分
#np.concatenate,np.vstack,np.hstack例程实现
#np.concatenate将数组元组或数组列表[x,y,z...]或者(x,y,z,...),x,y,z等是数组作为第一个参数
x = np.array([1,2,3])
y = np.array([3,2,1])
z = np.concatenate([x,y])
print(z)
#np.concatenate也可用于高维数组的拼接,参数附带一个数轴参数axis = ...,0表示按行拼接,1表示按列拼接
a = np.array([[1,2,3],
              [4,5,6]])
b = np.concatenate([a,a],axis = 0)
print(b)
    #np.vstack([x,y])和np.hstack([x,y])分别直接指定数组按行进行拼接和按列进行拼接
#数组的拆分
#使用np.split和np.vsplit,np.hsplit
#可以向以上函数传递一个索引列表作为参数,索引列表记录的是拆分点的索引位置,在索引前进行拆分
x = [1,2,3,4,99,99,5,6]
x1,x2,x3 = np.split(x,[2,6])
print(x1,'\n',x2,'\n',x3)
x = np.arange(0,20,2).reshape(5,2)
x1,x2 = np.hsplit(x,[1])
print(x1,'\n',x2)
x1,x2 = np.vsplit(x,[1])
print(x1,'\n',x2)


#通用函数介绍
#向量化操作,数组的运算
print(np.arange(5)/np.arange(1,6))
x = np.arange(10)
print(x**2)#相当于直接有个map函数作用在数组上
#Numpy的通用函数对于Python的加减乘除都可以使用
#对数组运用数学/逻辑运算相当于直接对数组中的每个元素进行运算
print(x + 5)
print(x - 5)
print(x * 5)
print(x / 5)
print(x % 5)
print(x ** 5)
print(x < 5)
print(-x,'\n',abs(-x))#绝对值函数
    #三角函数
theta = np.linspace(0,np.pi,3)#array([0,pi/2,pi])
print(np.array(np.sin(theta),dtype = int),np.cos(theta),np.tan(theta))#np.array(np.sin(theta),dtype = int)这样可以将数组中的整个数组进行数据类型的变换

#聚合运算
#通用函数的reduce方法会对一个数组的元素反复执行给定的运算,知道遍历完所有元素,得到最后的值
x = np.linspace(0,np.pi,6)
print(np.add.reduce(x),np.multiply.reduce(x),np.subtract.reduce(x))