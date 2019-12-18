#@author:leacoder
#@des:  动态规划 优化版 爬楼梯

'''
相对于动态规划 无优化会计算所有 dp[i]，这里每次迭代之和dp[i-1]和dp[i-2]有关
只存储当前以及上一个状态数据,空间复杂度 O(1) 时间复杂度O(n)
dp方程dp[i] = dp[i-1] + dp[i-2]，不必计算所有dp[i]
使用 f0 f1 分别为 上一状态， 当前状态
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        f0 = f1 = 1
        for i in range(1, n):
            f0, f1 = f1,f0 + f1
        return f1
