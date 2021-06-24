#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:return 0
        a = prices[0]
        b = 0
        c = 0 # 上次的股价
        n = [] # 盈利区间
        for p in prices:
            if p < c:
                a = p
                n.append(b)
                b = 0
            else:
                a = min(p,a)
                b = max(p-a,b)
            c = p
        n.append(b)
        n.sort()
        print(n)
        if len(n)>1:
            return n[-2]+n[-1]
        return n[0] if len(n)>0 else 0
# @lc code=end
s= Solution()
print(s.maxProfit([1,2,4,2,5,7,2,4,9,0]))
