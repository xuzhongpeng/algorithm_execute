#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
# 最右就是使用堆排序 建立 最小堆
from typing import List

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSort(nums,0,len(nums)-1)
        return nums[-k]
    def quickSort(self,nums:List[int],left,right):
        if left>=right: return
        standard,i,j = nums[left],left,right
        while i<j:
            while i<j and nums[j]>standard: j-=1
            while i<j and nums[i]<=standard: i+=1
            if i<j: nums[i],nums[j] = nums[j],nums[i]
        if nums[i]<standard: nums[i],nums[left] = nums[left],nums[i]
        self.quickSort(nums,left,i-1)
        self.quickSort(nums,i+1,right)
        # print(nums)

# @lc code=end

print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6],6))