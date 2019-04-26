#@author:leacoder
#@des:  动态规划  乘积最大子序列

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None : return 0
        res , curMax, curMin = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            curMax, curMin = curMax * num, curMin * num
            # 由于 num可能为负数 上面结果可能刚好反了, curMax * 负数变为 curMin 顾需要下面语句处理
            curMax,curMin = max(curMax,curMin,num),min(curMax,curMin,num)
            res = max(curMax,res)
        return res