#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def takeSecond(elem):
            return elem[0]
        intervals.sort(key=takeSecond)
        return self.merge1(intervals)
    def merge1(self,intervals):
        if len(intervals)<2: return intervals
        
        l = [intervals[0]]
        r = intervals[1:]
        while len(r)!=0:
            llast = l.pop()
            rfirst = r.pop(0)
            if llast[-1]>=rfirst[0]:
                l.append([llast[0],rfirst[-1] if rfirst[-1]>llast[-1] else llast[-1]])
            else:
                l.append(llast)
                l.append(rfirst)
        if len(l)!=0 and len(r)!=0:
            l.extend(r)
        return l
        # print(res)
        # print('***')
        # return res

# @lc code=end

s  = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))