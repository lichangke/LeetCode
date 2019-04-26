#@author:leacoder
#@des:  暴力求解  乘积最大子序列
# leetcode 超时

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxnum = float("-inf")
        for i in range(0,len(nums)):
            tmp = nums[i]
            for j in range(i+1,len(nums)):
                tmp *= nums[j]
                maxnum = max(maxnum,tmp)
            maxnum = max(maxnum,nums[i])
        return maxnum