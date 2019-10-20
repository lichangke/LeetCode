# @author:leacoder
# @des:  递归  合并两个有序链表

'''

重复处理单元：
比较两个链表节点值

递归终止条件：
两个链表都是空的

递归前处理（递归到下一层前处理）：
比较当前层 哪个链表头节点较小，递归找这个链表的下一个

递归（递归到下一层）：


递归后处理（下层递归返回后处理）：
返回较小值

'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1 
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2