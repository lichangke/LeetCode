
#@author:leacoder
#@des:  迭代 + 哨兵 反转链表 II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        result,cur ,prev,count =head, head ,None,1
        # 类似 206 cur 指向当前节点 ， prev 指向前一节点 result 记录头节点
        '''
        [1,2,3,4,5] m =2 n =4 为例
        '''
        '[1,m] 区间'
        # count < m 时 prev cur 依次移动  # 注意 边界 m = 1 时result prev 会有不同
        while count < m : 
            prev,cur,count = cur, cur.next ,count+1
        
        # last = cur = 2    prev = 1 
		# 衔接处理记录节点 last 记录 [m,n] 区间 翻转前的起始节点也就是[m,n] 区间 翻转后的尾节点 ，用于后续衔接使用
		# prev 为 [1,m] 区间 最后一节点 注意 m==1是为None
        tmp , last = None , cur #   tmp 哨兵 这样处理后 其 翻转 同 206
        
        '[m,n] 区间'
        while count <=n: # 反转
            cur.next,tmp,cur,count = tmp,cur,cur.next,count+1  
            
        # 循环结束后 tmp 为[m,n] 区间翻转后的起始节点，cur为[n,链表长度]区间起始节点 
        # [2 3 4] -> [4 3 2]  tmp = 4   cur = 5
        # 衔接处理  注意 m!=1 与 m==1
        if m != 1: # 
            prev.next = tmp # prev 为 [1,m] 区间 最后一节点   prev.next =  tmp 为[m,n] 区间翻转后的起始节点   pre = 1  tmp = 4  [1 4 3 2]
        else: # m==1 [1,m] 区间 没有 [m,n] 区间 为 [1 n],结果的头节点是 tmp 为[1,n] 区间翻转后的起始节点
            result = tmp
        '[n,链表长度]区间'  # last 记录 [m,n] 区间 翻转前的起始节点也就是[m,n] 区间 翻转后的尾节点
        last.next = cur # last.next 指向剩余的节点 cur为[n,链表长度]区间起始节点 
            
        return result

# 去掉注释
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head  
        result,cur ,prev,count =head, head ,None,1
        while count < m : 
            prev,cur,count = cur, cur.next ,count+1 
        tmp , last = None , cur 
        while count <=n: 
            cur.next,tmp,cur,count = tmp,cur,cur.next,count+1  
        if m != 1: # 
            prev.next = tmp 
        else:
            result = tmp
        last.next = cur  
        return result