import pandas as pd

df = pd.read_excel("info.xlsx", converters={'电话':str})
Class = df["班级"]
new_Class_test = []
for i in Class:
    i = str(i)
    i = i.replace("一","1").replace("二","2").replace("三","3").\
        replace("四","4").replace("五","5").replace("六","6").replace("七","7").replace("计科","计算机科学与技术")
    new_Class_test.append(i)
print(new_Class_test)
df["班级"] = new_Class_test
print(df)

"""
软件工程
计算机科学与技术
数据科学与大数据技术
网络工程
"""
