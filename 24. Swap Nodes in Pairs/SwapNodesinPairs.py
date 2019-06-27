# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None 
#@author:leacoder
#@des: 循环实现  多元赋值

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(None) # 哨兵
        retult,pre.next =pre, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next  # 记录 要交换的两节点
            pre.next,b.next,a.next,= b,a,b.next # 2个节点交换,注意哨兵的next改变了
            pre = a # 向下移动2位
        return retult.next