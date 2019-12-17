# @author:leacoder
# @des:  动态规划  买卖股票的最佳时机 II  (通用型)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        result = 0
        # 二维数组
        # profit[i][0] 第i天 没有股票 的利润
        # profit[i][1] 第i天 当前有股票  max（ 前面有股票今天不卖 ，前面没股票 今天买入 ） 的利润

        profit = [[0 for _ in range(2)] for _ in range(len(prices))]
        # 第一天利润初始
        profit[0][0] = 0
        profit[0][1] = - prices[0]

        for i in range(1,len(prices)):
            # 今天 无股票  max(前一天无股票今天不交易，前一天有股票今天卖出)
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] + prices[i])
            # 今天 有股票  max(前一天有股票今天不交易，前一天无股票今天买入)
            profit[i][1] = max(profit[i - 1][1], - prices[i])
            result = max(result,profit[i][0],profit[i][1])
        return result
