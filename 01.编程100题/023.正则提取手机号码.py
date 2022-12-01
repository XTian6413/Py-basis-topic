content = """
    白日依13888881881山尽,黄河入46525187891海流
    欲穷12345千里目,更13413537556上一层楼
"""

# 提取content中的手机号码   模式为 1开头 总共11位  第二位3-9
import re

# 写r的话不会被转义
pattern  = r'1[3-9]\d{9}'

results = re.findall(pattern,content)

print(results)  # 得到一个列表

for result in results:
    print(result)