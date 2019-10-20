#@author:leacoder
#@des: 递归实现   k个一组翻转链表

'''

重复处理单元：
k个一组翻转
链表可以分为 ： 待处理 + 当前层正处理（k个一组链表） + 下层递归已处理

下一层递归返回已处理头结点 
当前层就知道： 需要翻转k个一组链表的链表头、链表尾
链表头 head 参数
链表尾 遍历 k 个节点

递归终止条件：
后续迭代待处理剩余节点不足 k 个

递归前处理（递归到下一层前处理）：
k个一组翻转链表，下一次递归从 下 k 个节点开始
记录 翻转前的 链表头 链表尾

递归（递归到下一层）：
下k位，使用递归前处理的 链表尾.next


递归后处理（下层递归返回后处理）：
将下一层递归返回结果加入到原链表
K 个一组链表翻转，

'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 用于记录 翻转前的 链表头 链表尾
        end = head
        count = 0
        # 递归终止条件
        while end and count!= k:
            end = end.next
            count += 1
        if count == k:  # 递归终止条件
            # 递归前处理（递归到下一层前处理） 
            # 记录 翻转前的 链表头 head 链表尾 end 在前面已做
            # 递归（递归到下一层）：
            resultmp = self.reverseKGroup(end,k) # 下层 已处理头结点 
            # 递归后处理（下层递归返回后处理）
            while count:    # K 个一组链表翻转，
                tmp = head.next
                head.next = resultmp  # 将下一层递归返回结果加入到原链表
                resultmp = head
                head = tmp
                count -= 1
            head = resultmp # 翻转后链表头
        return head