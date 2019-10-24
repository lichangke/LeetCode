# @author:leacoder
# @des: 暴力法优化 柱状图中最大的矩形 O(n^2)
import sys
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 1:
            return heights[0]
        maxArea = 0
        for i in range(length):
            minHeight = sys.maxsize
            for j in range(i,length): 
                minHeight = min(minHeight,heights[j])
                maxArea = max(maxArea,minHeight * (j-i+1))

        return maxArea