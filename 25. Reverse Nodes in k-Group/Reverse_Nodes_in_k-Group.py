#@author:leacoder
#@des: 迭代实现   k个一组翻转链表

'''
利用哨兵简化操作
prev = ListNode(None) # 哨兵
prev.next = head
prev 每次迭代下移（下移位数为k）

重复处理单元：
k个一组翻转
链表可以分为 ：已处理 + 正处理（k个一组链表） + 后续迭代待处理
正处理（k个一组链表）需要知道 链表头和链表尾
链表头 可以通过 prev 的 next 获取
链表尾 需要遍历k个节点获取

迭代终止条件：
后续迭代待处理剩余节点不足 k 个

迭代前处理：
result 记录 prev 下移前的值 用于 结果返回
end 参数 记录尾节点
prev、end 每次迭代指向同一节点

迭代处理：
遍历k个节点获取 链表尾
构建 k个一组链表 并进行翻转 reverse()
reverse() 翻转函数返回 翻转后新链表头
将翻转后新链接入原链表
prev 下移 end 下移

迭代后处理：
无

'''

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 迭代前处理：
        prev = ListNode(None) # 哨兵
        prev.next = head
        result = prev
        end = prev  # end 记录 k个一组链表 链表尾  prev.next 记录 k个一组链表 链表头

        # 迭代终止条件：
        while(end.next): # 剩余节点不足 k 个
            for i in range(k): # 遍历k个节点获取 链表尾 并 判断 剩余节点 是否不足 k 个
                if not end: # 不足 k 个
                    break
                end = end.next
            if not end: # 不足 k 个
                break
            '''
            start = prev.next   # k个一组链表 链表头
            next = end.next     # 记录 原 end.next 
            end.next = None     # k个一组链表 链表尾
            '''
            # 构建 k个一组的链表
            start, next, end.next = prev.next, end.next, None
            # 翻转 k个一组的链表
            prev.next = self.reverse(start) # 返回 翻转后新链表头 接入原链表
            start.next = next  # 接入原链表  start 为 翻转后新链表尾
            prev = start
            end = start
        return result.next



    def reverse(self, head: ListNode):
        prev = None
        curr = head
        while(curr):
            '''
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            '''
            curr.next, prev, curr = prev, curr, curr.next
        return prev





