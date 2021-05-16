#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
import collections


class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,2)
obj.put(1,1)
obj.put(2,3)
obj.put(4,4)
param_1 = obj.get(1)
param_2 = obj.get(2)
param_6 = obj.get(1)
param_3 = obj.get(3)
param_4 = obj.get(4)
print('dd')
# @lc code=end

