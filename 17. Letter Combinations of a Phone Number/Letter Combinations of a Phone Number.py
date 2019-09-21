#@author:leacoder
#@des:  暴力法递归  电话号码的字母组合

"""
递归处理digits字符串中的每个字符
digits的每个字符又有多种情况（多个字母需要处理）
递归终止条件就是 digits字符串中的每个字符 已处理结束
"""

class Solution:
    phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
    output = [] # 输出
    def letterCombinations(self, digits: str) -> List[str]:
        
        # 字典 存储 每个数字对应的字母
        self.output = []
        if digits:
            self.recursive("",digits)	# "" 字母组合 最开始为"" , digits 待处理的字符串（处理后剩下的）
        return self.output

    #递归函数 
    # combination，上一层处理后的到的字母组合
    # next_digits，上层处理后剩余的字符串（本层需要处理的字符串）
    def recursive(self,combination , next_digits):
        if len(next_digits) == 0:	# 终止条件 字符串中的每个字母已处理结束
            self.output.append(combination)	# 将组合的字母组合存入output输出
            return
        else:
            for letter in self.phone[next_digits[0]]: # 处理 digits的每个字母 的多种情况
            	# combination + letter 将当前层处理的字母加入 字母组合
            	# next_digits[1:] 递归到 digits 字符串的下一个字符
                self.recursive(combination + letter,next_digits[1:])