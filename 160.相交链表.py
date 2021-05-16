#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
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
    # map 存值法
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        map = {}
        while headA is not None:
            map[headA] = 0
            headA = headA.next
        while headB is not None:
            if map.get(headB) is not None:
                return headB
            headB = headB.next
        return None
    # 循环链表解法
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr1, curr2 = headA, headB
        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA
        return curr1
# @lc code=end

n = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
a = ListNode(1,ListNode(2,n))
b = ListNode(1,ListNode(3,n))
s = Solution()
print(s.getIntersectionNode(a,b))