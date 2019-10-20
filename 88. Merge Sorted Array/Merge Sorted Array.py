# @author:leacoder
# @des:  合并后排序  合并两个有序数组
# 时间复杂度 : O((n + m)log(n + m))
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)

