#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
from typing import List

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quickSort(nums,0,len(nums)-1)
        nums.reverse()
        return '0' if nums[0]==0 else ''.join([str(x) for x in nums])
    def quickSort(self,nums:List[int],left:int,right:int):
        if left>=right: return nums
        standard,i,j = nums[left],left,right
        while i<j:
            while j>i and self.compare(nums[j],standard): j=j-1
            while j>i and self.compare(standard,nums[i]): i=i+1
            if j>i:
                nums[i],nums[j]=nums[j],nums[i]
        if self.compare(standard,nums[i]):
            nums[i],nums[left] =  nums[left],nums[i]
        self.quickSort(nums,left,i)
        self.quickSort(nums,i+1,right)
        return nums
    def compare(self,x:int,y:int):
        return str(x)+str(y)>=str(y)+str(x)

# @lc code=end

s=Solution()
print(s.largestNumber([10,2,9,39,17]))