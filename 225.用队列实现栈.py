#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start


import collections


class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.list.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.list.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.list)==0: return None
        return self.list[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.list)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(3)
# param_3 = obj.top()
# param_2 = obj.pop()
# param_4 = obj.empty()
# @lc code=end

obj = MyStack()
obj.push(3)
param_3 = obj.top()
param_2 = obj.pop()
param_4 = obj.empty()

# 可实现队列
queue1 = collections.deque()
queue1.append(1)
queue1.append(2)
queue1.append(2)
a = queue1.pop()
b = queue1.popleft()
print('x')