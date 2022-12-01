# 输入：
# [1,0,1]
# 返回值：
# 0

# a = [1, 0, 1, 0, 2]
a = [1, 0, 1]


class Solution(object):
    def singleNumber(self, nums):
        tagdict = {}
        for i in nums:
            if i in tagdict:
                tagdict[i] += 1
            else:
                tagdict[i] = 1

        for j in tagdict:
            if tagdict[j] == 1:
                return tagdict[j]


class Solution2(object):
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res


class Solution3(object):
    def singleNumber(self, nums):
        b = [i for i in nums if nums.count(i) == 1]
        return b

test_list = [1,1,1,2,2,2,3,3,3]
count = 0
for i in test_list:
    if test_list.count(i) == 3:  # 统计出现三次的数字
        count += 1

if count % 2 ==0:
    print((count//2)-2)
else:
    print((count//2)-1)