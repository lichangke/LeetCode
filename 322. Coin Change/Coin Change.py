# @author:leacoder
# @des:  动态规划 零钱兑换

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0 :    return -1
        DP = [amount + 1]*(amount + 1) #DP[i] 表示 总金额 为 i 时的最少硬币数，极限情况硬币数为 amount 不可能为 amount + 1
        DP[0] = 0 # 初始  下面 DP[i - coin]  中 i - coin = 0时
        for i in range(1,amount+1): # 总金额 1 到 amount 的循环
            for coin in coins: # 不同面额遍历
                if coin <= i: # 面额小于总金额
                    DP[i] = min(DP[i],DP[i - coin] + 1) # DP方程 类似70. 爬楼梯； 
        
        if DP[amount] == amount+1: 
            return -1
        else:
            return DP[amount]