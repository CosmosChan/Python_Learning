#异常和处理程序
#在我们自己不能提供自己的异常捕获代码时,使用try和except提供错误处理程序
#except
short_list = [1,2,3]
position = 6
try:
    short_list[position]
except:
    print('索引应该在0和%d'%(len(short_list)-1)+'之间,但却是%d'%position)
#在try中的代码会被执行,但是如果存在错误,就会抛出异常,然后执行except中的代码,否则跳过except块代码
#指定一个无参数的except适用于任何异常类型,如果可能发生多种类型的异常,最好时分开进行异常处理
#try:
#    语句块1
#except 异常类型1:
#    语句块2
#except 异常类型2:
#    语句块3
#....
#except 异常类型N:
#   语句块N+1
#except:
#   语句块N+2
#else:
#   语句块N+3
#finally:
#   语句块N+

#规则是这样的:如果try中的语句块发生错误,从except 语句块1开始查找,如果找到了
#则进入其提供的语句块进行处理,如果没有找到则直接进入except块进行处理,然后执行finally中的语句块(也就是一一查找,最后except托底)
#如果try中的语句块没有发生错误,则执行else中的语句块,然后执行finally中的语句块
#总之,无论是否发生错误,都要进入finally块中

#除数为0的异常处理
#x = int(input('请输入一个数字x: '))
#y = int(input('请输入一个数字y: '))
#try:
#    result = x/y
#except ZeroDivisionError:
#    print('除数不能为0')
#else:
#    print('%d/%d = %f'%(x,y,result))
#finally:
#    print('程序结束')
#常见的异常名称在P174
#读取文件时,输错文件名是常见的错误
#open()函数打不开一个文件时,会出现'OSError'异常
def open_file():
    while True:
        try:
            f = open(input('请输入文件名称:'),'rt')
            return f
        except Exception as name:#用这个来代替所有异常错误
            print('无法打开此文件或文件不存在,请重新输入文件名称')
f = open_file()
print(f.readlines())
f.close()
