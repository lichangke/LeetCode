#@author:leacoder
#@des:  动态规划 计算所有 f(n) 爬楼梯

'''
递推公式 f(n) = f(n-1) + f(n-2)
计算所有 f(n),空间复杂度 O(n) 时间复杂度O(n)

动态规划
a、重复子问题
当前台阶有 上1级跨1个台阶到达 或 上2级跨2个台阶到达
b、dp状态
dp[i]  到第i级台阶的不同走法
c、dp方程
dp[i] = dp[i-1] + dp[i-2]
初始化：
dp[0] = 1
dp[1] = 1
# 便于 i = 2 的推导

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]