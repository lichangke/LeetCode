# @author:leacoder
# @des:  贪心算法  买卖股票的最佳时机 II  时间复杂度 O（n）


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        for i in range(0,length):
            if i == length -1:
                return profit
            if prices[i]<prices[i+1]:
                profit += prices[i+1]-prices[i]
        return profit