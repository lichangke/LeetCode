# @author:leacoder 
# @des:  双指针解法 判断子序列

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    	# 判断 s 是否为 t 的子序列。
    	# 指针 point_s 指向 s 第一个字符，指针 point_t 指向 t 第一个字符。逐一判断 point_s 所指向的字符是否在 t 中存在。
    	point_s = 0
    	point_t = 0
    	length_s = len(s)
    	length_t = len(t)

    	'''
    	1、如果 s[point_s] != t[point_t] , point_t = point_t + 1, 继续对比t的下一个字符，s的第point_s个字符是否在t中
		2、如果 s[point_s] == t[point_t] , point_s = point_s + 1 , point_t = point_t + 1, 继续对比s的下一个字符。
    	'''
    	while point_s < length_s and point_t < length_t:
    		if s[point_s] == t[point_t]:
    			point_s = point_s + 1
    		point_t = point_t + 1


    	# 最后通过point_s是否与length_s相等判断s 是否为 t 的子序列。
    	return point_s == length_s
