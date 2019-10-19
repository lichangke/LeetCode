#@author:leacoder
#@des: 迭代实现  两两交换链表中的节点

'''
利用哨兵简化操作
 1->2->3->4
 2->1->4->3
 可参见 206 反转链表

'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode(None) # 哨兵
        prev.next = head
        retult = prev # 记录  第一次被操作前的prev 用于返回结果 
        while prev.next and prev.next.next: # 两两交换  其退出为 prev.next或prev.next.next 为空
            # 以 1 2 反转为例,prev为哨兵
            a = prev.next   # 由于 要操作 prev.next (1) 和 prev.next.next (2) 先记录下来
            b = prev.next.next  # 记录 要交换的两节点

            prev.next = b  # (2)
            a.next = b.next # (3)
            b.next = a  # (1)
            prev = a # (1) # 向下移动2位

            ''' 使用语法糖
            prev.next,a.next,b.next= b,b.next,a # 2个节点交换,注意哨兵的next改变了
            prev = a # 向下移动2位
            '''
        return retult.next