#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:return head
        res,temp,origin,tempHead=head,None,None,None
        i=1
        while head and i<=right:
            next = head.next
            # 如果左边的数是从中间开始的 加个标记
            if i+1 == left: 
                origin = head
            # 如果当前节点为开始节点 给temp赋值
            if i == left:
                temp = tempHead = ListNode(head.val)
            # 如果当前节点为需要反转节点
            elif temp and i<=right: 
                temp,temp.next = head,temp
            # 如果当前节点为结束节点 收尾链接起来
            if i == right:
                tempHead.next = next
                if origin:
                    origin.next = temp
                else:
                    res = temp
                break
            i += 1
            head = next
        return res

                

# @lc code=end

n = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
s = Solution()
print(s.reverseBetween(ListNode(5,ListNode(3)),1,2))