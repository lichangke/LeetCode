# @author:leacoder
# @des: 借助栈 有效的括号

'''
借助栈 stack
遍历 s
遇左括号入栈
遇右括号，与栈顶元素比较，是否匹配
    匹配 删除栈顶元素
    不匹配 失败返回
直到 s 遍历完
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {')':'(',']':'[','}':'{'}  #有配对情况 可以使用dict存储其键值对
        for c in s:
            if c not in paren_dict: #右括号类型 入栈
                stack.append(c)
            elif not stack: #如果这时栈已经空了 无效 注这个判断需要在下一个判断之前
                return False
            elif stack.pop()!= paren_dict[c]: #左括号类型 其paren_dict对应值需要与栈顶元素匹配 
                return False
        return not stack #s遍历完了  如果为空栈 有效 否则为无效