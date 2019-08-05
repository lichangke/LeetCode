# @author:leacoder
# @des:  暴力求解 最长回文子串

'''
从最长字符串开始扫描（最长子串就是其本身）子串个数为 1，如果不是回文 子串长度-1，子串个数+1

子串长度  子串个数
	n		1
	n-1		2
	.		.
	.		.
	2		n-1
	1		n
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if 0 == n:
            return Null
        for i in range(n): # i = 0 时为最长子串，长度n ；i = 1时 子串长度n-1子串个数2
            start = 0
            end = n - i # n-i 长度子串中，第一个子串的起始位置
            while end <= n:
                sub_string = s[start:end]	# 子串
                # 判断是否回文
                if self.is_palindromic_string(sub_string):
                    return sub_string
                # 遍历长度为 n-i 的所有子串
                start += 1
                end +=1

    def is_palindromic_string(self,s):
        return s == s[::-1]

