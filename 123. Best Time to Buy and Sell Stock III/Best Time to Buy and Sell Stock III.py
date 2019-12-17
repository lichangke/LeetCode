# @author:leacoder
# @des:  动态规划  买卖股票的最佳时机 III(通用型) 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        # 三维数组 
        # profit[ii][kk][jj] 
        # ii 第 ii 天， kk 股票操作了几次 ， jj 是否有股票
        # 最多可以完成 两笔 交易： kk 可以为 0 1 2 次操作 ， jj可以为 0 ，1    0 没有股票 1有股票
        profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        # 第一天 初始化 
        for k in range(3): #最多可以完成 两笔 交易 故range(3)
            profit[0][k][0] = 0 # 第 1 天 操作 k 次 没有股票，所以初始值为 0
            profit[0][k][1] = - prices[0] # 第 1 天 操作i 次 有股票， 所以初始值为 - prices[0]
       
        # 注意 买 卖 都进行一次算一次操作 k + 1,单独 买入 不算完成一次操作 以卖出 算一次操作（同理 可以 以买入 算一次操作，卖出时操作不计数）
        for i in range(1,len(prices)):
            # 第 i 天 0 次交易 没有股票最大利润 = 第 i-1 天 0 次交易 没有股票最大利润
            profit[i][0][0] = profit[i-1][0][0] 
            # 第 i 天 0 次交易 有股票最大利润 = max(第 i-1 天 0 次交易 有股票最大利润 , 第 i-1 天 0 次交易 无股票最大利润 - 当天股票价格prices[i]（买入）)
            profit[i][0][1] = max(profit[i-1][0][1],profit[i-1][0][0] - prices[i])
            
            # 第 i 天 1 次交易 无股票最大利润 = max(第 i-1 天 1次交易 无股票最大利润 , 第 i-1 天 0 次交易 有股票最大利润 + 当天股票价格prices[i]（卖出）)
            profit[i][1][0] = max(profit[i-1][1][0],profit[i-1][0][1] +prices[i] ) 
            # 第 i 天 1 次交易 有股票最大利润 = max(第 i-1 天 1 次交易 有股票最大利润 , 第 i-1 天 1 次交易 无股票最大利润 - 当天股票价格prices[i]（买入）)
            profit[i][1][1] = max(profit[i-1][1][1],profit[i-1][1][0] - prices[i])
            
            # 第 i 天 2 次交易 无股票最大利润 = max(第 i-1 天 2次交易 无股票最大利润 , 第 i-1 天 1 次交易 有股票最大利润 + 当天股票价格prices[i]（卖出）)
            profit[i][2][0] = max(profit[i-1][2][0],profit[i-1][1][1] + prices[i] ) 
            
        end = len(prices) - 1
        
        return max(profit[end][0][0],profit[end][1][0],profit[end][2][0])

