# @author:leacoder
# @des:  迭代  合并两个有序链表


'''
利用哨兵简化操作
prehead= ListNode(-1)

重复处理单元：
比较大小，将小的加入 prev

迭代终止条件：
两个链表任意一个为空

迭代前处理：
记录prev = prehead

迭代处理：
判断大小，加入prev的链表

迭代后处理：
处理 l1 或 l2 中剩余节点

'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 利用哨兵简化操作
        prehead= ListNode(-1)
        # 迭代前处理：
        prev = prehead # prev 用于迭代 这里记录表头 用于返回
        # 迭代终止条件：
        while l1 and l2:  #  两个链表任意一个为空
            # 迭代处理
            # 重复处理单元：
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next 
            prev = prev.next 
        # 迭代后处理：
        '''
        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2
        '''
        prev.next = l1 if l1 is not None else l2
        return prehead.next