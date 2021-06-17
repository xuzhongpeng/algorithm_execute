#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print('')
        x,y = 0,0
        i=0
        m = {}
        result = []
        while i<len(nums):
            if y==len(nums)-1:
                return result
            y = i + 1
            while y<len(nums):
                k = 0 - nums[i] - nums[y]
                if k in m:
                    print(m[k],k)
                if k in m:
                    m[k].append([i,y])
                else:
                    m[k] = [[i,y]]
                y += 1
            i += 1

# @lc code=end

Solution().threeSum([-1,0,1,2,-1,-4])