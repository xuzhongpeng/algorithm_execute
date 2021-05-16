#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        total = 0
        list = []
        while head is not None:
            total += 1
            list.append(head)
            head = head.next
        i =(total+1)//2 
        j = total % 2

        return list[i-j]
# @lc code=end
n = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
s = Solution()
print(s.middleNode(n))