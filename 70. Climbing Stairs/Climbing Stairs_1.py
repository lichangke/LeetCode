#@author:leacoder
#@des:  动态规划  爬楼梯

class Solution:
    def climbStairs(self, n: int) -> int:
        dicttmp = {0:1,1:1}
        if n == 1 or n == 0:
            return dicttmp[n]
        for i in range(2,n+1):
            dicttmp[i] = dicttmp[i-1] + dicttmp[i-2]  # 递推公式 f(n) = f(n-1) + f(n-2)
        return dicttmp[n]