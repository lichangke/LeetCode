#@author:leacoder
#@des:  动态规划  三角形最小路径和

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == None:
            return 0
        for i in range(len(triangle)-2,-1,-1): # 从下至上
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1]) 
                # DP状态方程：dp[i, j] = min(dp(i+1, j), dp(i+1, j+1)) + triangle[i, j]
        return triangle[0][0]