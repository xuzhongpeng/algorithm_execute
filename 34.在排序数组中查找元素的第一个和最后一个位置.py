#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.result = -1

        def dichotomy(nums: List[int], left, right):
            if left > right:
                return
            mid = (right+left) // 2
            # 找到一个数
            if nums[mid] == target:
                self.result = mid
                return
            elif nums[mid] > target:
                dichotomy(nums, left, mid-1)
            else:
                dichotomy(nums, mid+1, right)
        dichotomy(nums, 0, len(nums)-1)

        min, max = self.result, self.result
        if min != -1:
            while min >= 0 and nums[min] == target:
                min -= 1
            min += 1
            while max < len(nums) and nums[max] == target:
                max += 1
            max -= 1
        return [min, max]
# @lc code=end


print(Solution().searchRange([1], 1))
