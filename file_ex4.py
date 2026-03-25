import sys
import os
import math
#词频统计
#编写程序,统计一段英文文本,统计其中所有不同单词的个数,以及词频最大的10%的单词。
#所谓单词,是指由不超过80个单词字符组成的连续字符串,但长度超过15的单词将只截取保留前15个字符。
#合法的单词字符为大小写字母,数字和下划线,其他字符均认为是单词分隔符。
#str = str[:str.find('#')]
def char_range(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z') or ord(c) >= ord('A') and ord(c) <= ord('Z') or ord(c) >= ord('0') and ord(c) <= ord('9') or ord(c) == ord('_') or ord(c) == ord(' '):
        return True
    else:
        return False
def char_change(c):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return chr(ord(c) - ord('A') + ord('a'))
    else:
        return c
#os.chdir('D:/Python_Proj/Python_exercise')
#text = open('file_ex3.txt','w+t')
#text.write(input('请输入一段文本:'))
#print('指针位置为:',text.tell())
#text.seek(0)
#English_Text = text.read()
English_Text = sys.stdin.read()#输出一个字符串
print(English_Text)
word_dict = dict()
new_Text = str()
for i in range(len(English_Text)):
    if char_range(English_Text[i]) == False:
        new_Text += ' '
    else:
        new_Text += char_change(English_Text[i])
English_Text = new_Text
#print(English_Text)
English_Text = English_Text.split()#得到每个单词字符串组成的列表
#print(English_Text)
for i in English_Text:
    if len(i) > 15:
        i = i[:14]
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] += 1
#print(word_dict)
word_dict = sorted(word_dict.items(),key = lambda x:(-x[1],x[0]))
print(word_dict)
#text.close()