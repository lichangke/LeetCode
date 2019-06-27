#@author:leacoder
#@des: 递归实现  多元赋值
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        resultmp = self.swapPairs(head.next.next) # 下移两位  返回 值为两两交换后  两个节点中的前一个节点
        # 交换 当前两节点
        A, B = head, head.next # 当前两节点
        A.next, B.next = resultmp,A # 交换
        return  B   # 返回 两两交换后  两个节点中的前一个节点