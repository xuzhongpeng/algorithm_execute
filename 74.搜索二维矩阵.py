#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for n in matrix:
            for x in n:
                nums.append(x)
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
        if self.result!=-1: return True
        return False
# @lc code=end

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 4))
