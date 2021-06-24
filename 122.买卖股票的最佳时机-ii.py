#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:return 0
        a = prices[0]
        b = 0
        r = 0
        for p in prices:
            if b >= p:
                a = p
                r += b
                b = 0
            else:
                a = min(p,a)
                b = max(p-a,b)
        return r + b
# @lc code=end
s= Solution()
print(s.maxProfit([1,3,5,4,3,7,6,9,2,4]))

