# @author:leacoder
# @des:  暴力   旋转数组 O(n*k)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 旋转 k 次，每次将数组旋转 1 个元素。
        for i in range(k):
            prev = nums[len(nums)-1] # 从数组尾取数据
            for j in range(len(nums)):  # 将数组尾数据 放在数组头 并前后搬移数据
                temp = nums[j]
                nums[j] = prev
                prev = temp

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        # 旋转 k 次，每次将数组旋转 1 个元素。
        for _ in range(k):
             nums.insert(0, nums.pop())
