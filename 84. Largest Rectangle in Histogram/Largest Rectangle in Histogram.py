# @author:leacoder
# @des: 暴力法 柱状图中最大的矩形 O(n^3)

import sys
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 1:
            return heights[0]
        maxArea = 0
        for i in range(length):
            for j in range(i,length):
                minHeight = sys.maxsize
                for k in range(i,j+1):
                    minHeight = min(minHeight,heights[k])
                maxArea = max(maxArea,minHeight * (j-i+1))

        return maxArea
                