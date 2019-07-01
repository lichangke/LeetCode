# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# @author:leacoder 
# @des:  快慢指针 环形链表 II

class Solution(object):

    def getmeetnode(self,head):
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next  #慢指针 每次移一步
            fast = fast.next.next #快指针 每次移二步
            if slow == fast: 
                return slow # 找出相遇节点
        return None # 没有表示没有成环，返回None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        meetnode = self.getmeetnode(head)  # 找到 相遇时的节点meetnode
        if meetnode is None:  # 如果为None 表示不成环
            return None
        # 成环 由于 head->firstnode的节点个数 = meetnode->firstnode的节点个数
        cur1 ,cur2 = head,meetnode
        while cur1!=cur2:
            cur1,cur2 = cur1.next,cur2.next
        return cur1
