#@author:leacoder
#@des:  暴力法  盛最多水的容器

"""
两层循环遍历所有的可能解
时间复杂度： O(n*n) 空间复杂度：O(1)，使用恒定的额外空间。  leetcode 会超时失败
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
    	maxarea = 0	# 最大面积
    	length = len(height)
    	for i in range(0,length):	# 一层循环，确定容器左边
    		for j in range(i+1,length): # 二层循环，确定容器右边
    			tmparea = min(height[i],height[j])*(j-i) # 计算存水容量
    			maxarea = max(maxarea,tmparea)
    	return maxarea


