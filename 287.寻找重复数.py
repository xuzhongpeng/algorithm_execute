#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        base = 0
        for i in nums:
            if base == base | (1 << i):
                return i
            base |= (1 << i)
# @lc code=end

print(Solution().findDuplicate([1,2,4,5,4]))