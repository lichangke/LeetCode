# @author:leacoder
# @des: 递归实现 反转链表

'''
递归终止条件：
head.next 为 None
可以将 head 为 None 的特殊情况一起做判断
if not head or not head.next:
            return head
递归前处理：
这里只是反转链表而不是两两交换链表中的节点，不做处理。如题 24. 两两交换链表中的节点 、25. K 个一组翻转链表 则需要处理

递归：
p = reverseList(head.next)
这里 反转链表 顾 参数直接 next， 如题 24. 两两交换链表中的节点 、25. K 个一组翻转链表 则需要处理 会有不同 但是原理一样

递归后处理：
可以从后往前理解：
这里  p = reverseList(head.next) ， head.next 是结点 5 ，那么 当前 head 就是结点 4,  p 是结点 5 为反转后链表头，需不做操作从最底层返回出来
反转就需要 head.next (5) 的 next 指向 head (4) , head (4) 的 next 指向 None 与 之前 (1 2 3 结点)构成递归的上一层链表

1 -> 2 -> 3 -> 4 <- 5
            同时 4 -> NULL ， 递归的上一层链表 1 -> 2 -> 3 -> 4 -> NULL


待反转链表： 1 -> 2 -> 3 -> 4 -> 5 ->NULL
反转后链表：NULL <- 1 <- 2 <- 3 <- 4 <- 5


'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 递归前处理 ， 本题不做任何操作
        # 递归
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p




