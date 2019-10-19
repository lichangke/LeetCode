#@author:leacoder
#@des: 递归实现  两两交换链表中的节点

'''

重复处理单元：
两两交换
链表可以分为   待处理 + 当前层正处理（两两交换的两个节点） + 下层递归已处理

下一层递归返回已处理头结点
当前层就知道： 需要交换的 a、b 两节点 以及 后续已处理头节点


递归终止条件：
head.next 为 None
可以将 head 为 None 的特殊情况一起做判断
if not head or not head.next:
            return head

递归前处理（递归到下一层前处理）：
这里两两交换链表中的节点 ， 下一次递归从 下 两个的结点开始  题 25. K 个一组翻转链表 则另一种处理
可以记录下 当前的 next
next = head.next

递归（递归到下一层）：
下两位，使用递归前处理的 next
p = reverseList(next.next)   题 25. K 个一组翻转链表 则 会有不同 

递归后处理（下层递归返回后处理）：

1->2->3->4
2->1->4->3

'''

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归终止条件：
        if not head or not head.next:
            return head
        # 递归前处理（递归到下一层前处理）：
        # 当前层 需交换节点 为  head (a) 、head.next (b)
        next = head.next
        # 递归（递归到下一层）：
        resultmp = self.swapPairs(next.next) # 下移两位  返回值为两两交换后  两个节点中的前一个节点
        # 递归后处理（下层递归返回后处理）：
        head.next = resultmp  # 两两交换
        next.next = head  # 两两交换
        ''' 语法糖
        head.next, next.next = self.swapPairs(next.next), head
        '''
        return next   # 返回 两两交换后  两个节点中的前一个节点