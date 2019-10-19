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
        i = 1
        while cur: #遍历链表
            if i%k == 0: #k个一组 对这里面的数据翻转
                temp = cur.next #记录 后一个 k个一组的 头节点
                cur.next = None #赋值为None 前面 k个一组数据 为新的链表 以 None结束  
                end, start = self.reverse(pre.next)  #翻转新链表 返回头尾  注pre.next 为新链表翻转前的头
                pre.next = start  # 将翻转后的 链表头节点 赋值给 pre.next 链入按需要处理过的链表中
                end.next = temp #将翻转后的尾节点的next  end.next赋值为temp(后一个 k个一组的 头节点)  链入按需要处理过的链表中
                pre = end #pre 赋值为end 由于下一次循环 其 next为下一个 k个一组的头节点
                cur = temp #将之前 存下来的 后一个 k个一组的 头节点 赋值给 cur ，while循环下移
            else:
                cur = cur.next #我们关心k个一组的首尾
            i += 1
        return dim.next
    
    def reverse(self, head): #翻转链表
        dim1 = ListNode(0)
        dim1.next = head
        cur = head
        pre = None
        while cur: #遍历
            tmp = cur.next #存储 cur.next
            cur.next = pre #翻转 将 cur.next 赋值为pre
            pre = cur #pre移动
            cur = tmp #cur移动
        return dim1.next,pre    #翻转后end 和 start