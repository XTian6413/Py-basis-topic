content = """
提起风人们都不陌生，到处可见，可它喜怒无常，有时候像慈母一般，有时像调皮的孩子，有时像……
春天来了，风是那么的轻柔，它就像母亲一样轻轻唤醒熟睡了的孩子们，唤醒沉睡的大地，唤醒冬眠的动物。
到了夏天，风它就像一个调皮的孩子和我们玩起了捉迷藏游戏，一时找不到他的踪影，风，它会察言观色，当老天爷变脸的时候他比老天爷的脸变得还快，天上刚乌云密布，他马上就狂风大作，东、南、西、北，任他刮，似乎在告诉行人雨马上就要来了，老天爷露出了笑脸，风也温顺了，来到田野，西瓜熟了，来到池塘
里，荷花开了，来到……
到了秋天，风沙沙地吹，染黄了田野，染红了枫叶，还带来了一丝凉意，秋天的风总是发脾气，他怒了路旁的树木被它吹得摇摇摆摆，不时发出，呜呜哭声，沙沙沙……它吹过的树木一片片树叶再也受不了酷刑，马上从树枝上飘落下来，狂风又卷起沙子往空中抛，弄得街上的行人睁不开眼睛。
"""

import jieba
import jieba.posseg as posseg
import re
jieba.setLogLevel(jieba.logging.INFO)

content = re.sub(r'[\s，……、。]', "", content)

print(content)
n_word = []
# 该作文出现的名词为
print("出现的名词为:")
for word, flag in posseg.cut(content):
    if flag == 'n':
        print(word)
        n_word.append(word)

# 统计出现次数最多的前十个词语
import pandas as pd
count_n_word = pd.Series(n_word).value_counts()[:10]
print(count_n_word)

