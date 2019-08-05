# @author:leacoder
# @des:  动态规划 最长回文子串

'''
动态规划分析
一、状态定义
dp[l][r] 表示子串s[l,r] (包括区间l 和 r, l 表示子串左边索引，r 表示子串右边索引) 是否是回文，也就是如果s[l,r]是回文字符串，则有dp[l][r] = true
二、状态转移方程
1、如果s[l+1,r-1]长度大于 1,也就是 r-1 - (l+1)>0 -> r - 1 > 2 时，dp[l+1][r-1]=true 并且 s[l] == s[r] 那么 s[l,r] 为回文字符串 dp[l][r] = true
s[l+1,r-1]为回文字符串，只有当s[l] == s[r]时  s[l,r] 才为回文字符串
2、如果s[l+1,r-1] 长度为 1 也就是 r-1 - (l+1) = 0 -> r - l = 2 时 并且 s[l] == s[r] 那么 s[l,r] 为回文字符串 dp[l][r] = true
3、如果s[l+1,r-1] 为空字符串小于1也就是 r-1 - (l+1)< 0  -> r - l < 2，并且 s[l] == s[r] 那么 s[l,r] 为回文字符串，dp[l][r] = true
2 和 3合并为一个条件 r - l <= 2 并且 并且 s[l] == s[r]
所以 综上状态转移方程 为
s[l] == s[r] and (r -1 <= 2 or dp[l + 1, r - 1]) 那么 dp[l, r] = = true
'''
'''
特殊情况
当s字符串长度<=1时，其本身必然为回文字符串
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 特殊情况
        size = len(s)
        if size <= 1:
            return s
        # 状态 初始化 dp[l,r] 二维状态，初始化为False
        dp = [[False for _ in range(size)] for _ in range(size)]
		
		# 最长回文子串
        max_length = 0
        # max_substring = "" 
        max_substring = s[0] #  兼容处理 "ac" 这种情况
		# <=1 的情况 已在特殊情况中处理
        for r in range(1,size):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_length = r - l + 1 # 当前回文字符串长度
                    if cur_length > max_length:
                        max_length = cur_length
                        max_substring = s[l:r+1] # r+1取不到
        return max_substring