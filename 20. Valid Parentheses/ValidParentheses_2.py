# @author:leacoder
# @des: 借助栈 有效的括号

'''
辅助栈  stack
遍历字符串：
左括号 入栈
右括号 出栈并判断出栈元素是否与此右括号匹配
    匹配 continue
    不匹配 失败
    栈为空 失败
最后判断 辅助栈是否为空
'''


class Solution:
    def isValid(self, s: str) -> bool:
        data_dict = {')': '(', ']': '[', '}': '{'}  # 利用字典便于 判断是否匹配
        stack = []  # 辅助栈  stack
        for c in s:  # 遍历字符串
            if c not in data_dict:  # 不是 右括号 是左括号
                stack.append(c)
                continue
            if not stack:   # 有右括号 但是 栈为空 失败
                return False
            if stack.pop() != data_dict[c]:  # 不匹配 失败
                return False
        return not stack    # 最后判断 辅助栈是否为空
