# @author:leacoder
# @des:  动态规划  买卖股票的最佳时机 II  时间复杂度 O（n）

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        result = 0
        # 三维数组 
        # profit[i][0] 第i天 一直没有股票 的利润
        # profit[i][1] 第i天 当前有股票（ 前面有股票今天不卖 + 前面没股票 今天买入 ） 的利润
        # profit[i][2] 第i天 之前买入现在卖了   （前面有股票 今天卖出 ） 的利润
        profit = [[0 for _ in range(3)] for _ in range(len(prices))]
        # 第一天利润初始
        profit[0][0],profit[0][1],profit[0][2] = 0, - prices[0] , 0
        
        for i in range(1,len(prices)):
            profit[i][0] = profit[i - 1][0]
            profit[i][1] = max(profit[i - 1][1],profit[i - 1][0] - prices[i] )
            profit[i][2] = profit[i - 1][1] + prices[i] 
            result = max(result,profit[i][0],profit[i][1],profit[i][2])
        return result