#@author:leacoder
#@des:  双指针法  盛最多水的容器

"""
两线段之间形成的区域总是会受到其中较短那条长度的限制。此外，两线段距离越远，得到的面积就越大。
我们在由线段长度构成的数组中使用两个指针，一个放在开始（容器左边），一个置于末尾（容器右边）。
使用变量 maxarea 来持续存储到目前为止所获得的最大面积。每次移动指向较短线段的指针向较长线段那端移动一步（从两边向中间移动）。
为什要那样移动呢？
容器左边长为A，容器右边长为B，中间距离为（b-a）从两边向中间移动（容器左边更左，以及容器右边更右的情况，已经计算处理过了）。
当前面积为min(A,B) * （b-a）,从两边向中间移动中间距离必然减少，如果存在面积更大的情况，那么只能提高min(A,B) ，
那么只有将较短线段的指针向较长线段那端移动，才有可能存在新的A1，B1，中间距离为（b1-a1），使得min(A1,B1)* （b1-a1）更大。
(详细证明 https://leetcode-cn.com/problems/container-with-most-water/solution/shuang-zhi-zhen-fa-zheng-que-xing-zheng-ming-by-r3/)
时间复杂度： O(n) 一次扫描, 空间复杂度：O(1)，使用恒定的额外空间。 

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
    	maxarea = 0	# 最大面积
    	length = len(height)
    	left = 0
    	right = length - 1
    	while right > left:
    		heighttmp = min(height[left],height[right])
    		maxarea = max(maxarea, heighttmp * (right-left))
    		if height[left] < height[right]:
    			left = left + 1
    		else:
    			right = right - 1

    	return maxarea


