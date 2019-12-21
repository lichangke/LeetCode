# @author:leacoder
# @des: 迭代实现 反转链表

'''
1、先找重复处理单元
    每个结点 断开指向的下一个结点，next指针重新指向此结点的上一个结点
    A <-B C : 原顺序为 A B->C (A结点已被处理，当前处理B结点)
2、迭代终止条件
    到达尾结点
3、迭代前处理
    使用哨兵，记录每次处理结点的上一结点
4、迭代处理
    cur.next, prev, cur = prev, cur, cur.next
5、迭代后处理
    无
利用哨兵简化操作
NULL 1 -> 2 -> 3 -> 4 -> 5 ->NULL
NULL <- 1 <- 2 <- 3 <- 4 <- 5
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:    # 数据校验
            return None
        prev = None  # 利用哨兵
        cur = head
        while cur:
            # tmp = cur.next    # 我们要操作 cur ，断开其 next 指向的结点重新指向新的结点，这里先记录 cur.next 结点
            # cur.next = prev   # 重新 指向 cur.next 的结点为 prev
            # prev = cur     # prev 指向后移
            # cur = tmp     # cur 指向后移，后移的结点重复之前操作
            # 使用python 语法糖 简化
            cur.next, prev, cur = prev, cur, cur.next
        return prev

