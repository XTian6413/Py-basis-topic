# 输入文件
# 三列 学号 姓名 成绩
# 用逗号进行分割
# 行之间使用\n来分割
# 读取文件并进行排序

with open("012.信息.txt",mode="r",encoding="utf-8") as f:
    date = f.readlines()
# print(date) ['101,小张,88\n', '102,小王,77\n', '103,小李,99\n', '104,小赵,66\n', '105,小强,55']
# {'son': 101, 'sanme': '小张', 'sgrade': 89},
lst = []

for i in date:
    i = i.split(",")
    # 去除末尾的换行符
    i[2] = i[2].replace("\n","")
    d = {'id':i[0],'sname':i[1],'score':i[2]}
    lst.append(d)

new_lst = sorted(lst, key=lambda x:x['score'],reverse=True)
print(new_lst)
