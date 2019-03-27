# @author:leacoder
# @des:   借助dic 两数之和 O（N）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):#循环  O(N)
            diff = target - nums[i]
            if diff in nums[i+1:]: #O(1)
                return [i,nums[i+1:].index(diff)+i+1]
        return []