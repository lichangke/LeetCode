# @author:leacoder
# @des: 迭代实现 反转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        prev = None # 利用哨兵
        cur = head
        while cur:

            '''
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            使用python 语法糖 简化
            '''
            cur.next, prev, cur = prev, cur ,cur.next
        return prev