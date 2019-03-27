# @author:leacoder
# @des:   暴力循环  两数之和  O(N*N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1,num1 in enumerate(nums):  #两层循环
            for index2,num2 in enumerate(nums[index1+1:]):
                if num1 + num2 == target:
                    return [index1,index1+index2+1]
        return []
            
        