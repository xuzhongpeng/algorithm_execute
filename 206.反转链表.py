#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = None
        while head is not None:
            t = head.next
            head.next = temp
            temp = head
            head = t
        return temp
# @lc code=end

s = Solution()
print(s.reverseList(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))