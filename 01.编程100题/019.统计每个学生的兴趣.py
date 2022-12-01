# key是球类 value是数字
like_count = {}
with open("019.student_like.txt",mode="r",encoding="utf-8") as f:
    for i in f.readlines():
        i = i.replace("\n","")
        i = i.split(",")
        del i[0]  # 将姓名删除
        for like in i:
            if like not in like_count:
                like_count[like] = 0
            like_count[like] += 1
print(like_count)

y = []
x = []
for key in like_count:
    y.append(like_count.get(key))
    x.append(key)

# 作图
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

plt.pie(y,
        labels=x, # 设置饼图标签
        explode=(0.2, 0, 0, 0.2, 0),
        colors=['#FF0000','#BBFF66','#33FFAA','#B088FF','#666666'],
        autopct='%.2f%%',
        shadow=True
       )
plt.title("学生信息爱好统计",fontsize = 18) # 设置标题
plt.show()

# plt.title("学生信息爱好展示",fontsize=20,loc='center')
# plt.xlabel("x - label")
# plt.ylabel("项目",fontsize=18)


# 绘制条形图
# plt.bar(x, y, color ='#0000FF',width=0.6)
# plt.show()