import math
#文件读写分为以下三个操作
#1.打开文件
#2.处理数据
#3.关闭文件
#打开文件open()
#fileobj = open(file_name,mode,encoding = None)
#mode的第一个字母表明对其的操作
import os 
os.chdir('D:/python_Proj')#change directory
textFile = open('text.txt','r')
#t = textFile.readline()
t1,t2 = (textFile.read()).split('\n')
#print(t)
print(t1,t2)
textFile.close()
textFile = open('text.txt','rb')
print(type(textFile))
b = textFile.readline()
print(b)
textFile.close()
print(os.getcwd())


#文件打开模式:
#r:只读模式
#w:只写模式(如果没有该文件则创建一个文件,并重写新内容,如果已有文件,覆盖之前文件内容重新写),指针放在最前面
#a:追加模式(如果有该文件则追加内容,没有则创建一个文件),指针放在文末
#x:创建模式(如果该文件已存在则报错,不存在则创建一个新文件)
#b:二进制模式
#+:与r/w/a/x一起使用,增加读写功能
#t:文本模式(默认)
#b:二进制模式
#文件处理模式:
#open():打开文件

#参数名.read([size]):读取指定的字节数,如果未给定或为负则读取所有内容,返回字符串
#参数名.readline():读取一行内容,返回字符串
#参数名.readlines():读取所有行并返回列表
#参数名.write(string):写入字符串,默认使用UTF-8编码
#参数名.writelines(sequence):向文件写入一个元素为字符串的列表,如果需要换行则要加入每行的换行符
#参数名.tell():返回当前位置
#参数名.seek(offset[,whence]):移动文件指针,参数offset为偏移量,参数whence为0表示从文件开头开始算起,1表示从当前位置开始算起,2表示从文件末尾开始算起
#参数名.close():关闭文件
#注意:同一个文件参数textFile不能同时既读又写,可以读设置一个文件参数,写再设置一个文件参数

#先打开文件(或者创造文件)
#处理文件(写或读,处理指针位置)
#关闭文件
os.chdir('D:/Python_Proj/Python_exercise')
textfile = open('file_ex1.txt','w+t')#这边需要注意如果后续还需要读写操作不能只写w或者r或者wt,rt,中间最好附带着'+'
textfile.write('97 80 93 69 87 90 84 94 75 76 89\n86 80 85 73 82 86 76 83 65 77 90\n88 98 91 89 67 83 87 98 96 84 91')
textfile.seek(0)#重新定位文件指针的位置
info = textfile.read()
textfile1 = open('file_ex1_copy.txt','w+t')
textfile1.write(info)
textfile.seek(0)#很重要
info1 = textfile1.read()
textfile1.writelines('5201314cjj')
print(info,'\n',info1)
textfile.close()
textfile1.close()
print(os.getcwd())

#例2
os.chdir('D:/Python_Proj/Python_exercise')
f1 = open('file_ex2','w+t')
for i in range(5):
    #s = input('请输入学生姓名,学生学号,学生笔试分,学生平时分和学生实验分:')
    s = str(5201314)
    f1.writelines(s+'\n')
    print(f1.tell())
f1.seek(0)
print(f1.tell())
f1.write('1234\n')
print(f1.tell())
text = f1.read()
print(text)
f1.close()

#用键盘输入readlines()
import sys
string = sys.stdin.readlines()#按下ctrl-Z,再按Enter键结束输入
print(string)

