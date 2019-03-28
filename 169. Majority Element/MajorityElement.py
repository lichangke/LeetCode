# @author:leacoder
# @des:  排序法 求众数  时间复杂度 O（nlg(n)）

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        nums.sort()
        return nums[int(len(nums)/2)]  #条件>n/2，所以排序后，中间元素一定是众数

