#@author:leacoder
#@des:  斐波拉契 无优化  爬楼梯

'''
递推公式 f(n) = f(n-1) + f(n-2)
就是一个Fibonacci, 这里 是不做任何优化的递归实现的斐波拉契
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.recursive(n)

    # 递归
    def recursive(self, n:int) -> int:
        # 递归终止条件
        if n == 0 or n == 1 or  n == 2:
            return n
        return self.recursive(n-1) + self.recursive(n-2)

