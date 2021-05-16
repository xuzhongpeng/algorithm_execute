#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#
import collections
# @lc code=start
class FreqStack:

    def __init__(self):
        # 用于计算出现次数  对象（key-int）保存输入数字及数字出现的次数
        self.freq = collections.Counter()
        # 用于存储值 对象（key-数组）保存出现次数，及输入的数们
        self.group = collections.defaultdict(list)
        # 最大频率数
        self.maxfreq = 0  

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        # 这里为什么不用操作当前已经被pop的数，因为之前已经记录过了，直接用
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
obj.push(3)
param_2 = obj.pop()
# @lc code=end

