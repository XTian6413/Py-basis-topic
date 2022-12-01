# 依旧使用012.信息作为测试信息
socre = []
score_info = []
with open("012.信息.txt", encoding="utf-8") as f:
    for i in f:
        i = i.split(",")
        i[2] = i[2].replace("\n", "")
        d = {'id': i[0], 'name': i[1], 'score': i[2]}
        score_info.append(d)
        socre.append(i[2])
# 添加到列表中,每循环一次就是一个字典-> 根据键来获取值(获取max/min/判断是否存在) -> 排序
print(max(socre))
print(min(socre))

# 排序后的字典
d = sorted(score_info, key=lambda x: x['score'], reverse=True)
print("最高分学生的信息为", d[0])

# 使用遍历来打印信息
# 遍历字典得到的是key
# 而通过key可以取得value

for key in d[0]:
    print(key + ":" + d[0][key])

print("最低分学生的信息为", d[-1])

# 统计学生总数
print("学生总人数为:", len(d))
