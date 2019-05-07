# @author:leacoder
# @des:  一次遍历  买卖股票的最佳时机 II  时间复杂度 O（n）
# 由于一次交易操作 故可以通过记录最小价格 计算最大利润的方式

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        minprice,maxprofit = float("inf"),0
        
        for i in range(len(prices)):
            minprice = min(minprice,prices[i]) # 记录当前最小
            maxprofit = max(maxprofit,prices[i] - minprice) # 计算 当前最大利润（之前最大利润 与 当前价格与之前最小价格之差 的最大值）
        return maxprofit