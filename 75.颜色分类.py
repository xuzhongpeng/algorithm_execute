#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while i!=len(nums) and j!=len(nums):
            n = nums[i]
            if n == 0:
                nums.pop(i)
                nums.insert(0,n)
                i += 1
                j += 1
            elif n == 2:
                nums.pop(i)
                nums.append(n)
                j += 1
            else:
                i += 1
                j += 1
        print(nums)
# @lc code=end

print(Solution().sortColors([1,1,0,0,2,2,2]))