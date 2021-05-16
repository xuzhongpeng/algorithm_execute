#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        ''' 采用双指针法
            - slow指向前面一个奇数节点 fast往后寻找下一个奇数节点 找到后移到slow后面
        '''
        if not head or not head.next or not head.next.next:return head
        # slow慢指针 fastHead记录fast指针前节点 fast 快指针
        slow,fastHead,fast = head,head.next,head.next.next
        # fast指针的节点位置
        i = 3
        while fast:
            if i % 2 == 1:
                # 将fast指向的节点移动到slow指针后
                fastHead.next,slow.next,fast.next =fast.next,fast,slow.next
                # slow指针指向当前fast
                slow = fast
                # fast指针指向原来的位置
                fast = fastHead
            i += 1
            fastHead = fast
            fast = fast.next
        return head
# @lc code=end

n = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))
s = Solution()
print(s.oddEvenList(n))