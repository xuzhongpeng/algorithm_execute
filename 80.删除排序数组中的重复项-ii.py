#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        count = 1
        i = 1
        while i<len(nums):
            n = nums[i]
            if n == nums[i-1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                else:
                    i += 1
            else:
                i += 1
                count = 1
        return len(nums)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         dic = {}
#         i = 0
#         while i<len(nums):
#             n = nums[i]
#             l = dic.get(n)
#             if l is not None:
#                 dic[n]+=1
#                 if l > 1:
#                     nums.pop(i)
#                 else:
#                     i+=1
#             else:
#                 i+=1
#                 dic[n] = 1
#         return len(nums)
# @lc code=end


print(Solution().removeDuplicates([0,0,1,1,1,1,1,2,3,3]))


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) < 2: return len(nums)
#         count = 1
#         i = 1
#         while i<len(nums):
#             n = nums[i]
#             if n == nums[i-1]:
#                 count += 1
#                 if count > 2:
#                     nums.pop(i)
#                 else:
#                     i += 1
#             else:
#                 i += 1
#                 count = 1
#         return len(nums)