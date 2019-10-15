#@author:leacoder
#@des:  动态规划 计算所有 f(n) 爬楼梯

'''
递推公式 f(n) = f(n-1) + f(n-2)
计算所有 f(n),空间复杂度 O(n) 时间复杂度O(n)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dictways = {0:1,1:1,2:2}
        if n == 0 or n == 1:
            return dictways[n]
        for i in range(2,n+1):
            dictways[i] = dictways[i-1] + dictways[i-2] # 递推公式 f(n) = f(n-1) + f(n-2)
        return dictways[n]