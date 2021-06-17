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
            y = i + 1
            while y<len(nums):
                z = nums[y]
                if z in m and len(m[z]) != 0:
                    for r in m[z]:
                        if r.count(y) == 0:
                            l  = []
                            for n in r:
                                l.append(nums[n])
                            l.append(z)
                            result.append(l)
                            m[z].remove(r)
                    break
                k = 0 - nums[i] - nums[y]
                if k in m:
                    m[k].append([i,y])
                else:
                    m[k] = [[i,y]]
                y += 1
            i += 1
        return result

# @lc code=end

print(Solution().threeSum([-1,0,1,2,-1,-4]))