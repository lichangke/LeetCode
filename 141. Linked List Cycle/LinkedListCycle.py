# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# @author:leacoder
# @des:  存储记录 环形链表

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        save = set() #用于 存储 链表中每个节点地址
        cur = head
        while cur is not None: #循环迭代链表
            if cur in save: #是否有记录
                return True #有返回True
            else:
                save.add(cur) #存储记录cur
                cur = cur.next #下移
        return False