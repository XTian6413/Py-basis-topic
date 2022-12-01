lst = [
    {'son': 101, 'sanme': '小张', 'sgrade': 99},
    {'son': 101, 'sanme': '小张', 'sgrade': 78},
    {'son': 101, 'sanme': '小张', 'sgrade': 100},
    {'son': 101, 'sanme': '小张', 'sgrade': 89},
]

studen_sort = sorted(lst, key=lambda x:x['sgrade'])


for i in lst:
    print(i)
print('-------------------------------')
for i in studen_sort:
    print(i)
