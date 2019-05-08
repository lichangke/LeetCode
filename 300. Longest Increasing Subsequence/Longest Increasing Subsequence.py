# @author:leacoder
# @des:  动态规划 最长上升子序列  时间复杂度 O(n*n) 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        result = 1
        DP = [1 for i in range(len(nums))] # DP[ii] 表示 从 0 到 ii 且 第ii元素nums[ii]被选入最长上升子序列 的 序列长度  至少 为 1
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 表示 序列为上升的 DP[j] 第j元素nums[j]被选入最长上升子序列 的 序列长度
                    DP[i] = max(DP[i],DP[j] + 1) # 这时 nums[i] 被选入，长度 + 1。max 找出 第 0 到 i 元素 被选入最长上升子序列 的 序列长度 的 最大值
            result = max(result,DP[i])
        return result

