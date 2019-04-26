#@author:leacoder
#@des:  动态规划  乘积最大子序列

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None : return 0
        res , curMax, curMin = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            if num < 0 :
                curMax, curMin = curMin, curMax # 由于 num为负数 导致最大的变最小的，最小的变最大的,因此交换两个的值
            curMax = max(curMax*num,num)
            curMin = min(curMin*num,num)
            res = max(curMax,res)
        return res