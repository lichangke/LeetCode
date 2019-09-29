# @author:leacoder
# @des:  按字典顺序生成 下一个排列

'''
1、先找出最大的索引 firstIndex 满足 nums[firstIndex] < nums[firstIndex+1]，如果不存在，就翻转整个数组；
2、再在索引大于firstIndex中找出第一次另一个最大索引 secondIndex  满足 nums[secondIndex ] > nums[firstIndex]；
3、交换 nums[secondIndex] 和 nums[firstIndex]；
4、最后翻转 索引大于firstIndex的数组 nums[firstIndex+1:]。
参考：
https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        firstIndex = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]: # 找出最大的索引 k 满足 nums[k] < nums[k+1]
                firstIndex = i
                break

        if -1 == firstIndex: # 如果不存在
            self.reverse(nums, 0, n-1)
            return
        secondIndex = -1

        # 在索引大于firstIndex中,找出secondIndex第一次使 nums[secondIndex ] > nums[firstIndex]
        for i in range(n-1,firstIndex,-1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        # 交换 nums[secondIndex] 和 nums[firstIndex]；
        nums[firstIndex],nums[secondIndex] = nums[secondIndex],nums[firstIndex]
        # 翻转 索引大于firstIndex的数组 
        self.reverse(nums, firstIndex+1, n-1)
		
    # 翻转数组
    def reverse(self,nums,i,j):
        while i < j:
            nums[i],nums[j] = nums[j], nums[i]
            i += 1
            j -= 1	