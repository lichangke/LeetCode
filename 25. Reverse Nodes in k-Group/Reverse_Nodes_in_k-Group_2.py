# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# @author:leacoder
# @des: 借助单链表翻转  k个一组翻转链表

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head #由于遍历
        dim = ListNode(0) #新建一节点 
        dim.next = head #next指向head
        pre = dim #pre 赋值为 dim  1、记录和获取 k个一组的头 2、方便统一处理
        # pre 与 dim 均为哨兵
        count = 1
        while cur: #遍历链表
            if count % k == 0: #k个一组 对这里面的数据翻转
                nextstart = cur.next #记录 后一个 k个一组的 头节点
                cur.next = None #赋值为None 前面 k个一组数据 为新的链表 以 None结束 这个新链表可以采用206的处理方式
                end, start = self.reverse(pre.next)  #翻转新链表 返回翻转的  尾 和 头  注pre.next 为新链表翻转前的头
                # 衔接处理，哨兵的next指向翻转后的头， 翻转后的尾的next指向nextstart， pre 和 cur 依次下移k个元素 变为 end 和 nextstart下一轮处理就变成本轮一样了
                pre.next,end.next,pre,cur = start,nextstart,end,nextstart
            else:
                cur = cur.next #我们关心k个一组的首尾
            count += 1
        return dim.next
    
    def reverse(self, head): #翻转链表
        dim1,cur,pre = head,head,None
        while cur: #遍历
            cur.next,pre,cur  = pre,cur,cur.next
        return dim1,pre    #翻转后end 和 start