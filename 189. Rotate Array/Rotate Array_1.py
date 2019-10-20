# @author:leacoder
# @des:  拼接切片 使用额外的数组  旋转数组 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n # 处理 k > len(nums)的情况
        # 切片 nums[-k:] ：后 k个数据  nums[:-k] : 前 len(nums) - k 个数据
        nums[:] = nums[-k:] + nums[:-k]