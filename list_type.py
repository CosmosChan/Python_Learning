import math
#a = [1,2,3,4,5]
#b = a[1]
#c = ['1','2','3','4','5']
#print(a,'\n',b,'\n',c)
#print(type(a),'\n',type(b),'\n',type(c[1]))
#
##列表list
#构建列表
#a = []
#a = list()
##添加列表元素
#
##1.列表的append()方法:一次只能添加一个元素,并且只能添加到列表的末尾,采用 变量名.append(元素值) 方法
#a.append(6)
#print(a)
#a.append('7')
#print(a)
##2.列表的extend()方法:一次可以添加一个或多个元素,并且可以添加到列表的末尾,采用 列表名.extend([元素列表]) 方法
#a.extend([8,9,10])
#print(a)
#a.extend(['11','12'])
#print(a)
##3.列表的insert()方法:一次可以添加一个元素,并且可以添加到列表的指定位置,采用 列表名.insert(索引,元素值) 方法
#a.insert(0,'0')
#print(a)
#a.insert(5,'cjj love dwh')
#print(a)
#列表构建的推导式
#lst = [expression1 [if condition2 else expression2] for item in iterable [if condition1]]
#它与下面的语句等价
#lst = []
#for item in 列表:
#    if condition1:
#       if condition2:
#           lst = lst + [expression2 of item]
#       else:
#           lst = lst + [expression3 of item]
print(sum([1/i for i in list(range(1,21))]))

#如果要输出1-1/2+1/3-1/4+1/5-1/6....+(-1)**(n-1)/n
print(sum(1/i if i % 2 == 0 else -1/i for i in range(1,21)))

#如果要输出1-1/3+1/5-1/7+...+(-1)**(n-1)/(2n-1)
print(sum(1/i if i % 4 == 1 else -1/i for i in list(range(1,21,2))))
#或者
print(sum(1/i if i % 4 == 1 else -1/i for i in range(1,21) if i % 2 == 1))#与上面的表达式等效

#如果要输出6 + 66 + 666 + 6666 + ... + 6...6(n个6)
#列表生成 list(6 * 10**(i-1))会发现需要迭代,这无法用一句的表达式来实现
#通过字符串的方法可以实现
print(sum(int('6'* i) for i in range(1,11)))

a = list('cjj love dwh')
print(a)

b = list((1,2,3,4))
print(b)

d = str([1,2,3,4])

c = {1: 'cjj',2 : 'dwh',3:'yzw'}
c['linrui'] = 'c'
print(c)

e = dict(name = 'cjj' , age = 18)
print(e)
del e['name']
b.pop(1)
print(e)
print(b)


#join函数的用法:separator.join(iterable)
#用于对可迭代对象(元素为字符串类型)进行将分隔符separator和各个元素连接起来
print('*'.join('cjj love dwh'))
#转换字符串类型的数据到int类型的数据用map()函数,对iterable中的每个元素进行映射
print(','.join(map(str,range(10))))

#
#
#
##删除列表元素
##1.del()方法:删除指定索引位置的元素,采用 del 列表名[索引] 方法
#del a[0]
#print(a)
#del a[4]
#print(a)
#
##2.列表的remove()方法:删除指定元素,采用 列表名.remove(元素值) 方法,且只删除第一个出现的列表元素值
#a.remove('7')
#print(a)
#del a[9]
#print(a)
#a.insert(8,'9')
#print(a)
#
##3.列表的pop()方法:删除列表索引处的元素,采用 列表名.pop(索引值) 方法,但pop()也可以表示删除列表末尾处的元素
#b = a.pop(0)#删除第0个索引处的元素
#print(a,'\n',b)
#b = a.pop(9)
#print(a,'\n',b)
#b = a.pop()
#print(a,'\n',b)
#
#
##列表切片：切片是指对操作的对象截取其中一部分的操作,列表切片就是对指定列表截取某些元素的操作
##语法格式: 列表名[start:end:step],含义是从start开始到end-1结束,以步长为step,即每隔step个单元截取一个元素,如果省略step,则默认步长为1进行截取
##如果省略start(冒号:不能省略),则默认从列表的开头开始截取元素,如果省略end,则默认截取到列表末尾
##Tips:如果省略start,end的值,将step的值设为-1,即列表名[::-1]可以获得整个列表的逆序
#print(a[::2])
#print(a[1:9])
#print(a[::-1])
#
#
##列表之间的运算:+ ; * ; 比较 ; 逻辑
#b = a[2:5]
#print(a+b,'\n',b)
#print(a*2 + b)
#print(a>b)
#print(a<b)
#print(a>b and a!= b)
#
#del a,b
#
##二维列表:二维列表的元素也是列表,比如二维列表a = [[1,2,3],[4,5,6],[7,8,9]]
#
#
##元组tuple
#构建列表 
a = ()
print(type(a))
b = tuple()
print(type(b))
##元组和列表一样,也是有序的,但元组中的元素不能被修改,元组中的元素不能被删除,元组中的元素不能被添加,元组中的元素不能被替换,元组中的元素不能被排序,元组中的元素不能被去重,元组中的元素不能被清空
##且元组的定界符是圆括号(),元组中的元素用逗号隔开
#x1 = (1,2,3,'cjj','cjj love dwh')
#x2 = (True,False)
#print(type(x1),'\n',type(x2))
#print(x1,'\n',x2)
#
##删除元组del 元组名
##del x1,x2
##访问元组与访问列表一样,通过元组名[(start):(end)(:step)]
#x3 = x1[::2]
#print(x3)
#del x3
#
#x3 = x1+x2
#print(x3)
##del x3
#x3 = x3 * 2
#print(x3,'\n',len(x3))
#del x3
#
#
##字典dict
#定义字典
a = dict()
print(type(a))
a = {}
print(type(a))
##字典的定界符是一对花括号,字典是一种无序的,可变的序列
##字典的每一个元素内容都是必须由键和值两部分组成,键与值的间隔符为冒号,字典的每个元素值之间仍然用逗号隔开
##字典名 = {键1:值1,键2:值2,键3:值3,键4:值4,键5:值5...}
##字典中的键不能使用列表,值可以是任意类型的数据。同一个字典中的值可以重复,但键不能重复,如果键重复则选择后一个键
#z1 = {'name':'cjj','sex':'male','age':18}
#z2 = {'name':'dwh','sex':'female','age':17}
#z3 = {'name':'yzw','sex':'male','age':18}
#z4 = {('name','sex','age'):['cjj','male',18],(1,2,3):[1,2,3]}
#z = [z1,z2,z3]
#print(z1,'\n',z2,'\n',z3,'\n',z)
#print(z4)
#print(type(z1))
#print(type(z2))
#print(type(z3))
#print(type(z))
#
##del z1,z2,z3,z4,z
#
##访问字典中元素的方法为访问字典中的键 字典名[键]
##由于字典是无序的,所以访问字典中的元素时,不能使用索引,只能使用键访问字典中的元素
#print(z1['name'],'\n',z2['sex'],'\n',z3['age'],'\n',z4[('name','sex','age')],'\n',z[1])
##删除字典中的元素:del 字典名[键]
#del z1['name']
#print(z1)
#del z1['sex']
#print(z1)
#del z1,z2,z3,z4,z
##访问字典中的元素还可以用dict.get(键[,默认值])
#dict_1 = {'name':'cjj','sex':'male','age':18}
#dict_1.get('name')
#
##如果要访问字典中所有键值和数值,可以使用dict.keys()和dict.values()
#dict_1 = {'name':'cjj','sex':'male','age':18}
#a = dict_1.keys()#类型作为字典键值组成的视图对象
#b = dict_1.values()
#print(a,b,type(a))
#print(list(zip(a,b)))
#
##添加或修改字典中的元素:字典名[键] = 值
##如果是已知键,则进行替换,如果是未知键,则进行添加(在字典末尾添加)
#z1 = {'name':'cjj','sex':'male','age':18}
#z1['name'] = 'dwh'
#z1['height'] = 172
#print(z1)
#del z1
#
##检查字典中是否有某个关键字可以用(关键字 in 字典名)作为一个Bool值
#
#
##集合set
##集合的创建
a = set()#只能这样创建一个空集合
print(type(a))
#set()#创建一个空集合
#set({1,2,3,4,5})
#a = {1,2,3,4,5,'cjj'}
#b = a | {1,2,3,4,5}
#a.update({'name':'cjj','sex':'male'})
#print(a)          
#print(b)
#print(a)
#a.pop()
#print(a)
#a.remove('name')
#print(a)
#
##del a,b
#
##集合的运算:& / - in
#a = {1,2,3,4,5}
#b = {4,5,6,7,8}
#print(a & b)
#print(a|b)
#print(a-b)
#print(b-a)
#print(1 in a)
#print(8 in b)
#
#a.add('cjj')
#b.update('cjj')#这就是add()与update()的区别
#print(a , '\n' , b)
#
##列表list实训操作
##2.(1)
#aihao = ['旅游','看书','听歌']
#aihao.append('网络游戏')
#print(aihao)
#print('所有爱好是:',aihao)
#print('第二个爱好是:',aihao[1])
#del aihao
##2.(2)
#list1 = [12,3,48,6,79,63,89,7]
#print(list1[::-1])
#list1.sort()
#print(list1)
##list1.reverse()
#print(list1[::-1])
#del list1
##2.(3)(4)(5)(6)(7)
#list2 = [1,2,3,4,5,6,7,8,9,10]
#a = list2[::2]
#b = list2[1::2]
#c = a + b
#d = b + a
#print(a,'\n',b,'\n',c,'\n',d)
#del list2
##2.(8)
#list3 = [1,2,3,4,5,6,7]
#t1 = int(len(list3)/2)
#t2 = len(list3)/2
#t3 = round(t2)
#print(list3[t1],'\n',t1,t2,t3)
#
##元组,字典,字符串操作
##2.(1)
#tuple1 = (1,2,3,4,5,6)
#print(len(tuple1),max(tuple1),min(tuple1))
##2.(2)
#dict1 = {'231880075':'cjj','231880074':'lr','231880073':'yzw','231880072':'ww','231880071':'qq'}
#print(dict1,dict1['231880074'],len(dict1))
##2.(3)
#string1 = 'cjjlovedwh'
#A = string1[::2]
#B = string1[1::2]
#print(A,B,A+B)
##2.(4)
#print(string1[::-1])
##2.(5)
#string2 = 'cjj lov dwh'
#t = (int)(len(string1)/2)
#print(string2[t])
##2.(6)
#list2 = []
#dictA = {'name':'cjj','age': 21 ,'sex':'male'}
#dictB = {'name':'dwh','age': 20 ,'sex':'female'}
#dictC = {'name':'yzw','age': 21 ,'sex':'male'}
#list2.insert(0,dictA)
#list2.insert(1,dictB)
#list2.insert(2,dictC)
#print(list2)