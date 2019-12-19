# @author:leacoder
# @des:   借助两数之和  三数之和

class Solution(object):
    def threeSum(self, nums):
        nums.sort() #排序 方便去重
        res = []
        for i, num in enumerate(nums): #一层循环
            if i > 0 and nums[i] == nums[i-1]: # 避免重复
                continue
                
            new_nums = nums[i+1:] #剔除 一层循环后的数 
            two_sums = self.twoSum(new_nums, -num) #由于和为0  两数之和要为 -num
            for two_sum in two_sums:
                res.append([num, new_nums[two_sum[0]], new_nums[two_sum[1]]])
                         
        return res
            
        
    def twoSum(self, nums, target):
        d = {}
        res = []
        hit = False
        for i, num in enumerate(nums):
            if i > 1 and nums[i] == nums[i-1] and hit:
                continue
            if num in d:
                res.append([d[num], i])
                hit = True
            else:
                d[target - num] = i
                hit = False
        return res