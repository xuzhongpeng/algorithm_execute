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
        i = 0
        for p in prices:
            a = min(p,a)
            b = max(p-a,b)
            i += 1
        return b
# @lc code=end
s= Solution()
print(s.maxProfit([7,6,5,4,3]))
# @lc code=end

