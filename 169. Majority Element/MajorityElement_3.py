# @author:leacoder
# @des:  分治 求众数

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        def helper(left,right):
            if left == right:
                return nums[right]

            mid = (right-left)//2 + left

            leftval = helper(left, mid)
            rightval = helper(mid+1, right)

            if left == right:
                return left
            left_count = sum(1 for i in range(left, right+1) if nums[i] == leftval)
            right_count = sum(1 for i in range(left, right+1) if nums[i] == rightval)

            return leftval if left_count > right_count else rightval

        return helper(0, len(nums)-1)