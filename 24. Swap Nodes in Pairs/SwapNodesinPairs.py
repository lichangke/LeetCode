#@author:leacoder
#@des: 迭代实现  两两交换链表中的节点

'''
利用哨兵简化操作
 1->2->3->4
 2->1->4->3
 可参见 206 反转链表


重复处理单元：
两两交换
链表可以分为   已处理 + 正处理（两两交换的两个节点） + 后续迭代待处理

迭代终止条件：
两两交换，迭代处理这两个节点，那么后续节点不足两个时跳出迭代
prev.next ，prev.next.next 为 None 

迭代前处理：
利用哨兵简化操作，添加哨兵节点 prev
最终结果  以 2->1->4->3 为例 其头节点为 2  
由于两两交换 prev 也会跟随下移，先 用 retult = prev 记录prev下移前的值用于最终结果返回

迭代处理：
 1->2->3->4 为例
将需要翻转操作的两个节点记录（要断开连接，先记录）
a = prev.next   (1) 
b = prev.next.next  (2)
交换两节点
prev 节点下移，迭代开始新一轮处理 （由于两两交换，跳过两个节点）

迭代后处理：
无特殊处理

'''

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        # 迭代前处理：
        prev = ListNode(None) # 哨兵
        prev.next = head
        retult = prev # 记录  第一次被操作前的prev 用于返回结果

        # 迭代终止条件 prev.next ，prev.next.next 为 None 
        while prev.next and prev.next.next: 
            # 迭代处理：
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
        # 迭代后处理 无
        return retult.next