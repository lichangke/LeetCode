# @author:leacoder
# @des:  动态规划  买卖股票的最佳时机 II


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        maxprof = 0
        profit = [[0 for _ in range(2)]  for _ in range(0, len(prices))]
        # DP[ii][0] 第ii天 无股票的利润 DP[ii][1]第ii天有股票的利润 prices[ii] 第ii天股票价格
        profit[0][0] = 0  # 第 1 天没有股票，所以初始值为 0
        profit[0][1] = - prices[0]  # 第 1 天  有股票， 所以初始值为 - prices[ii]

        for ii in range(1, len(prices)):  # 天数
            # 今天 无股票  max(前一天无股票今天不交易，前一天有股票今天卖出)
            profit[ii][0] = max(profit[ii - 1][0], profit[ii - 1][1] + prices[ii])
            # 今天 有股票  max(前一天有股票今天不交易，前一天无股票今天买入)
            profit[ii][1] = max(profit[ii - 1][1], profit[ii - 1][0] - prices[ii])
            maxprof = max(maxprof, profit[ii][0])
        return maxprof