#@author:leacoder
#@des:  动态规划  爬楼梯

class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = f1 = 1
        for i in range(1,n):
            f0,f1 = f1, f0+f1 # 递推公式 f(n) = f(n-1) + f(n-2)只关心 f(n-1) + f(n-2)不必要所有f
        return f1