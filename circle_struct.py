import math

#分支结构
#1.if ... elif ... else
#str_num = input("请输入三个数字(请以空格隔开):")
#[a,b,c] = str_num.split()
#a = int(a)
#b = int(b)
#c = int(c)
#if a+b>c & a+c>b & b+c>a:
#    print("构成三角形")
#else:
#    print("不构成三角形")
#循环结构
#while,for
#实训项目1.(1)
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += -i
    else:
        sum += i
print(sum)

#实训项目1.(2)
price_a = 5
price_b = 3
price_c = 1/3
num_a , num_b , num_c = 0,0,0
for num_a in range(0,101):
    for num_b in range(0,101):
        if (100 - num_a*5 - num_b*3)/(1/3) == (100 - num_a - num_b):
            print('公鸡有%d只,母鸡有%d只,小鸡有%d只'%(num_a,num_b,100-num_a-num_b))

#实训项目1.(3)
#for i in range(100,1000):
#    if i % 3 == 0:
#        print(i)

#实训项目1.(4)
reading_speed = 0
rest_pages = 1000
while rest_pages >= 0:
    reading_speed += 1
    rest_pages += -reading_speed
print('小明读了%d天'%reading_speed)

sum = 0
for i in range(1,46):
    sum += i
print(sum)


