#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
from typing import List
# 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = {}
        for i in set(nums):
            l[i] = 0 
        for i in nums:
            l[i] += 1
        l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
        ll = []
        for key, value in l.items():
            ll.append(key)
            k -= 1
            if k == 0:
                break
        return ll
# @lc code=end
print(Solution().topKFrequent([1,1,1,2,2,3],2))
