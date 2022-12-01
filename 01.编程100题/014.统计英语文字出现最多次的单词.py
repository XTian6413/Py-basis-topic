d ={}
with open("014.countword", encoding="utf-8") as f:
    data = f.read()
    data = data.replace("\n", "").replace(",","").replace(".", "")
    data = data.split(" ")

print("一共有", len(set(data)), "个单词")

for word in data:
    word = word.lower()  # 先全部转化为小写
    try:
        d[word] += 1
    except:
        d[word] = 1

# 降序输出 出现次数前前十的单词
data = sorted(d.items(),key=lambda x:x[1],reverse=True)[:10]
for item in data:
    print("单词",item[0],"出现了:",item[1])