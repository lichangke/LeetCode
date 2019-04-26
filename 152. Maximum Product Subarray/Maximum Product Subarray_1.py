#@author:leacoder
#@des:  动态规划  乘积最大子序列

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None : return 0
        imax = [0,0] 
        imin = [0,0]
        imax[0], imin[0],res= nums[0],nums[0],nums[0]
        
        for i in range(1,len(nums)):
            x,y=i%2,(i-1)%2 # x 表示当前最大或最小下标   y 表示前面最大或最小下标
            imax[x] = max( imax[y] * nums[i], imin[y] * nums[i], nums[i] ) 
            # nums[i]可能为负数，若为负数 前面最小 *  nums[i]变为最大，前面最大 *  nums[i]变为最小
            imin[x] = min( imax[y] * nums[i], imin[y] * nums[i], nums[i] ) 
            res = max(res,imax[x])
        return res