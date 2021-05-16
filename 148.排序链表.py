#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        fast,slow  = head.next,head
        while fast and fast.next: fast,slow = fast.next.next,slow.next
        mid,slow.next= slow.next,None
        left = self.sortList(head)
        right = self.sortList(mid)
        #  对left和right进行排序
        temp = res = ListNode(0)
        # print("###")
        # self.printNode(left)
        # print("####")
        # self.printNode(right)
        while  left and  right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = left if left else right
        # print("****")
        # print(res.next.val)
        return res.next

    def printNode(self,node:ListNode):
        if node is None or node.val is None:return
        print(node.val)
        self.printNode(node.next)

# @lc code=end


node = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0)))))
Solution().printNode(Solution().sortList(node))