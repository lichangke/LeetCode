
# @author:leacoder
# @des: 借助栈  k个一组翻转链表
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        result= ListNode(None)
        cur,result.next = head,head
        tmpresult = result
        stack = [] # 列表实现栈的 先入后出功能
        count = 0

        while cur:
            count = count + 1
            stack.append(cur) # 入栈
            cur = cur.next
            if count % k == 0: # 已存储k个元素
                count = 0
                while stack: # 出栈倒换
                    tmpresult.next = stack.pop()
                    tmpresult = tmpresult.next

        # 处理 stack 中剩余元素
        while stack:
            tmpresult.next = stack.pop(0) # 
            tmpresult = tmpresult.next 
        return result.next