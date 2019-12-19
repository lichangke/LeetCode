# @author:leacoder
# @des:   暴力求解  三数之和
'''
3层循环 O(n^3)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = len(nums)
        result = list()
        nums = sorted(nums)     # 排序 用于后面去重
        for i in range(count-2):
            for j in range(i+1,count-1):
                for k in range(j+1,count):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i],nums[j] ,nums[k]] not in result:    # 去重
                            result.append([nums[i],nums[j] ,nums[k]])
        return result