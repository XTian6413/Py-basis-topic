content = """
    白日依13888881881@qq.com山尽,黄河入46525187891#abc.com海流
    欲穷12345@163.com千里目,更python1355@sina.net上一层楼
"""

import re
# 形式:  字母数字 @ .

pattern = r"[a-zA-z0-9_-]+@[a-zA-z0-9]+\.[a-zA-z]{2,4}"

results = re.findall(pattern, content)

for result in results:
    print(result)
