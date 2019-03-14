# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur:
            cur.next,prev,cur = prev,cur,cur.next
        return prev
 #利用python中有一种赋值机制即多元赋值，采用这种方式赋值时，等号两边的对象都是元组并且元组的小括号是可选的
 # x, y, z = 1, 2, 'a string'
 # 等同于 (x, y, z) = (1, 2, 'a string') 
 # 这种赋值类型最经常用到的环境是变量交换，形如
 # x, y = y, x
