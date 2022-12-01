import re
import pandas as pd
with open('014.countword',mode="r", encoding="utf-8") as f:
    content = f.read()

# 逗号 问号 句号 括号 全部作为分割的标识
word_list = re.split(r'[\s.()-?]+', content)


# 输出出现最多且位前20的单词 用dict转化为字典
count_word = dict(pd.Series(word_list).value_counts()[:20])

# key 为单词
# value 为单词出现的次数
keys = []
value = []
for key in count_word:
    keys.append(key)
    value.append(count_word.get(key))
print(keys)
print(value)

# 开始做条形图
import matplotlib.pyplot as plt
plt.figure(dpi=180)
plt.title('单词出现次数统计',color='#9955FF')
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.xticks(range(1,17),fontsize=10)
plt.barh(keys,value)
plt.show()