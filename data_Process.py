import pandas as pd
from plotly import figure_factory as ff
#在文件处理操作中一般都是用的表格的形式存储数据,表格在pandas中用DataFrame表示
data_frame = pd.DataFrame([['陈佳俊',21,'231880075','男',119,140,135],\
                        ['颜子为',21,'231880073','男',123,139,130],\
                        ['林锐',21,'231880074','男',115,135,145],\
                        ['杜玮晗',20,'231880520','女',150,150,150]]\
                        ,columns = ['name','age','id','sex','chinese_score','math_score','english_store'])
print(data_frame)
print(data_frame['name'])
print(data_frame.loc[0,'age'])#location
print(data_frame.at[3,'name'])
print(data_frame.iloc[0:2])#integer location,左闭右开原则
data_frame['total_score'] = data_frame['chinese_score'] + data_frame['math_score'] + data_frame['english_store']
figure = ff.create_table(data_frame)
figure.show()