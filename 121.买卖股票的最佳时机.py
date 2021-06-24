#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        b = 0
        for p in prices:
            a = min()
# @lc code=end
s= Solution()
print(s.maxProfit([7,1,5,3,6,4]))
