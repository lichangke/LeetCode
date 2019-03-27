# @author:leacoder
# @des:   一层枚举 左右两指针形式  三数之和 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index1,value in enumerate(nums[:-2]): #一层循环
            if index1>0 and nums[index1] == nums[index1-1]: #不可以包含重复的三元组
                continue
            left,right = index1+1,len(nums)-1  #左右指针形式  左：一层数据右侧开始  右:数据最右端开始
            while left<right: #循环条件  依据实际大小情况，选择左或右指针向中间移动  但右必定大于左
                sumtmp = nums[index1] + nums[left] + nums[right] #三数和
                if sumtmp <0: left +=1 # <0 表明和小了，那么左指针向右+1 真大 nums[left]  nums已经排序 右边必定大于 左边
                elif sumtmp >0: right -=1 #同上 
                else: #刚好为0
                    res.append((nums[index1],nums[left],nums[right]))
                    while left < right and nums[left]==nums[left+1]: #不可以包含重复的三元组
                        left +=1
                    while left < right and nums[right]==nums[right-1]:#不可以包含重复的三元组
                        right -=1
                    left +=1;right -=1
        return res
                