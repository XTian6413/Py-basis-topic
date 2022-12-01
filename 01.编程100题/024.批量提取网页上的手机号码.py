# 模式 1开头 2-9为第二位 总共11位
import re
with open('024.num_phone.txt',mode="r", encoding='utf-8') as rf:
    content = rf.read()

pattern = r'1[3-9]\d{9}'
results = re.findall(pattern,content)

for result in results:
    print(result)
else:
    print('总共有',len(results),"个手机号码")