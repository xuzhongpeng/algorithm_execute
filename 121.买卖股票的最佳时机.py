#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:return 0
        a = prices[0]
        b = 0
        i = 0
        while i < len(prices):
            a = min(prices[i],a)
            b = max(prices[i]-a,b)
            i += 1
        return b
# @lc code=end
s= Solution()
print(s.maxProfit([7,6,5,4,3]))
