#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 快慢指针
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
# @lc code=end

n = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
a = ListNode(1,ListNode(2,n))
b = ListNode(1,ListNode(3,n))
s = Solution()
# print(s.getIntersectionNode(a))