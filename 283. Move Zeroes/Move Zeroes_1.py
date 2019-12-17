# @author:leacoder
# @des:  双指针  移动零

'''
i：用于遍历 整个数组
j: 指向非0数位置
遍历数组，将非0数填入j所在位置j后移
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)  # 数组长度
        notzeroIndex = 0   # 移动后 非零元素起始位置
        for i in range(length):
            if nums[i] != 0:
                nums[notzeroIndex] = nums[i]
                if i != notzeroIndex:  # 不等置零
                    nums[i] = 0
                notzeroIndex = notzeroIndex + 1
