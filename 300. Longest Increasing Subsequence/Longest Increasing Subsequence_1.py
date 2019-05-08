# @author:leacoder
# @des:  维护子序列+二分查找 最长上升子序列  时间复杂度 O(n log n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        tails = [0] * len(nums)
        size = 0 # 最长上升子序列长度
        for num in nums:
            i , j = 0 , size 
            while i != j: # 二分查找 num 插入位置
                m = int((i + j)/2)
                if tails[m] < num : 
                    i = m + 1 # 查找后半段  
                else:
                    j = m # 查找前半段
            # i 为数据插入位置 ，可能 1、已有替换 2、后面新增替换
            tails[i] = num #
            # 这之前 size 为 num 插入前 最长上升子序列长度
            size = max(i+1,size) # 1、已有替换 size > i+1   2、后面新增替换   size < i+1
        return size
                    