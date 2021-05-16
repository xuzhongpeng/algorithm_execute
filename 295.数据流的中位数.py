#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq
# @lc code=start


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.max_heap)==len(self.min_heap):
            return (-self.max_heap[0]+self.min_heap[0])/2
        else:
            return -self.max_heap[0]
# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)
# @lc code=end
