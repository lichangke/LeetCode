# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# @author:leacoder
# @des:  快慢指针 环形链表

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next  #慢指针 每次移一步
            fast = fast.next.next #快指针 每次移二步
            if slow == fast: 
                return True
        return False