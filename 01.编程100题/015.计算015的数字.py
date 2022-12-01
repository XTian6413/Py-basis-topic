s = """
56
270
106
197
141
211
231
270
175
462
388
73
642
753
1258
545
285
"""
Sum = 0
s = s.split('\n')
print(s)
for i in s:
    if i == "":
        continue
    else:
        Sum += int(i)
print(Sum)