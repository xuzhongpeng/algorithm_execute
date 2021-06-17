#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# 要做過才會知道解法
# 主要就是每一次先固定最左邊的數字不要動，當作標準
# 剩下的就使用左右指標來找解

# Ex : 
# [ -3, -2, 0, 1, 2, 3]
#    S   L           R
# -3 當標準不動

# L/R 當雙指標向內移動
# [ -3, -2, 0, 1, 2, 3]
#    S      L     R
# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print('')
# @lc code=end

print(Solution().threeSum([-1,0,1,2,-1,-4]))