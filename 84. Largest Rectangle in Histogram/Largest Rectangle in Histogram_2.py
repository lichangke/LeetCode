# @author:leacoder
# @des: 栈 柱状图中最大的矩形   O(n)

'''
维护一个栈,把 -1 放进栈的顶部来表示开始
heights 按照从左到右的顺序，我们不断将柱子的序号放进栈中，直到遇到相邻柱子呈下降关系，新元素小于栈顶元素
这是不断出栈并计算 最大面积 然后 再 比较新元素与 栈顶元素 重复此操作

将新元素入栈

heights 序号处理完
处理栈中剩余元素
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0
        length = len(heights)
        # 按照从左到右的顺序,处理 柱子的序号
        for i in range(length):
            # stack[-1] 数据已处理完
            # heights[stack[-1]] >= heights[i]   新元素小于栈顶元素
            while stack[-1]!=-1 and heights[stack[-1]] >= heights[i]:
                maxArea = max(maxArea , heights[stack.pop()] * (i-stack[-1] - 1))
            # 将新元素入栈
            stack.append(i) 

        # 处理栈中剩余元素
        while stack[-1]!=-1:
            maxArea = max(maxArea,heights[stack.pop()]*(length-stack[-1] - 1))

        return maxArea