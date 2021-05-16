#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.listA = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        listB = []
        while len(self.listA)!=0:
            listB.append(self.listA.pop())
        self.listA.append(x)
        while len(listB) != 0:
            self.listA.append(listB.pop())
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.listA.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():return None
        return self.listA[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.listA) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(5)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print('')
# @lc code=end

