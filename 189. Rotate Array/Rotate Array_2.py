# @author:leacoder
# @des:  翻转  旋转数组 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n # 处理 k > len(nums)的情况
        
        nums[:] = nums[::-1] # 整体翻转
        nums[:k] = nums[:k][::-1] # 前 k 翻转
        nums[k:] = nums[k:][::-1] # 剩余翻转
