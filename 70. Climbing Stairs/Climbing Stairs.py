#@author:leacoder
#@des:  动态规划  爬楼梯

'''
只存储当前以及上一个状态数据,空间复杂度 O(1) 时间复杂度O(n)
递推公式 f(n) = f(n-1) + f(n-2)只关心 f(n-1) f(n-2)不必要所有f(n)
f0 f1 分别为 上一状态当前状态
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = f1 = 1
        for i in range(1,n):
            f0,f1 = f1,f1 + f0
        return f1