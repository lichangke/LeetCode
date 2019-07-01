# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# @author:leacoder 
# @des:  哈希表 环形链表 II

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        nodes.add(None)
        cur = head
        while cur not in nodes:
            nodes.add(cur)
            cur = cur.next
        return cur