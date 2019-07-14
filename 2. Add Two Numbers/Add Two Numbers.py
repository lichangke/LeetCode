# @author:leacoder
# @des:  迭代——哨兵 两数相加

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre1 = ListNode(None) # 哨兵
        pre2 = ListNode(None)
        pre1.next = l1
        pre2.next = l2
        # next_add进位位（cur_val_1+cur_val_2的十位数）, cur_val_1当前加数, cur_val_2当前被加数, cur_result当前存储位（cur_val_1+cur_val_2的个位数）
        next_add, cur_val_1, cur_val_2, cur_result = 0, 0, 0, 0
        result = ListNode(None)
        head = result
        while (pre1.next is not None) or (pre2.next is not None):
            # 注意对于 next 是否为 None 的处理不同
            if pre1.next is None:
                cur_val_1 = 0
            else:
                cur_val_1 = pre1.next.val
                pre1 = pre1.next
            if pre2.next is None:
                cur_val_2 = 0
            else:
                cur_val_2 = pre2.next.val
                pre2 = pre2.next
            val_sum = cur_val_1 + cur_val_2 + next_add
            next_add = val_sum // 10
            cur_result = val_sum % 10
            node = ListNode(cur_result)
            result.next = node
            result = result.next
        # 最高位进位处理
        if next_add != 0:
            node = ListNode(next_add)
            result.next = node
        return head.next