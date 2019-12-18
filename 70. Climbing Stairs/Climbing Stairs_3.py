#@author:leacoder
#@des:  斐波拉契 备忘录  爬楼梯

'''
递推公式 f(n) = f(n-1) + f(n-2)
就是一个Fibonacci, 这里 使用 字典 存储 斐波拉契数列 递归中重复计算项
'''

class Solution:
    def climbStairs(self, n: int) -> int:
       self.value_dict = dict()     # 字典
       return self.recursive(n)

    # 递归
    def recursive(self, n:int) -> int:
        # 递归终止条件
        if n == 0 or n == 1 or n == 2:
            return n
        if n in self.value_dict:
            return self.value_dict[n]
        result = self.recursive(n - 1) + self.recursive(n - 2)
        self.value_dict[n] = result     # 存入字典
        return result

