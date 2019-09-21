#@author:leacoder
#@des:  迭代  电话号码的字母组合

"""
迭代digits字符串中每个字符num进行处理
遍历 phone[num] 中每个字母并加入现有结果中得到新的结果
digits字符串中num字符处理结束（phone[num] 中每个字母处理完成）更新现有结果
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
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        output = [""] # 输出 初始 存储""
        for num in digits:	# 对digits字符串中每个字符进行处理
            tmplist=[]	# 中间变量
            for letter in self.phone[num]: # 遍历 phone[num] 每个字母进行处理
                for tmp in output:	# 遍历output向输出中添加新增的字母
                    # 注意 tmp + letter，tmp在前 因为新增的字母要加在后面
                    tmplist.append(tmp + letter)	
            output = tmplist # digits字符串中num字符处理结束（phone[num] 中每个字母处理完成）更新现有结果
        return output

"""
把代码块
for num in digits:	# 对digits字符串中每个字符进行处理
    tmplist=[]	# 中间变量
    for letter in self.phone[num]: # 遍历 phone[num] 每个字母进行处理
        for tmp in output:	# 遍历output向输出中添加新增的字母
            # 注意 tmp + letter，tmp在前 因为新增的字母要加在后面
            tmplist.append(tmp + letter)	
    output = tmplist # digits字符串中num字符处理结束（phone[num] 中每个字母处理完成）更新现有结果

可以精简为：
for num in digits:
	output =   [tmp + letter  for letter in self.phone[num] for tmp in output]
"""