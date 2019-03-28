# @author:leacoder
# @des:  摩尔投票法 求众数

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        moore = 0
        count = 0
        for num in nums:  #由于给定的数组总是存在众数。 众数 与 非众数 抵消后最后 count必然>0
            if count == 0:
                moore = num #最终 moore 存放的就是众数
            if num == moore:
                count +=1  #重复一次 +1
            else:
                count -=1 #出现其他数据 -1
        return moore