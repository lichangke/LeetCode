# @author:leacoder
# @des:  dic 求众数

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] = dic[num]+1
            else:
                dic[num] = 1
        length = len(nums)
        for num in dic:
            if dic[num]>int(length/2):
                return num