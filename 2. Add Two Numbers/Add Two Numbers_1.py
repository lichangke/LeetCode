# @author:leacoder
# @des:  递归+哨兵 两数相加
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addNumbers(l1, l2, 0)
    
    def addNumbers(self, l1: ListNode, l2: ListNode, add_num: int):
        if l1 is None and l2 is None and add_num == 0: # 递归终止条件
            return None
        l1_value = l2_value = 0
        if l1 is None:
            l1_value = 0
        else:
            l1_value = l1.val
            l1 = l1.next

        if l2 is None:
            l2_value = 0
        else:
            l2_value = l2.val
            l2 = l2.next
        sum_num = l1_value + l2_value + add_num
        result = ListNode(sum_num % 10)
        result.next = self.addNumbers(l1, l2, sum_num // 10)
        return result