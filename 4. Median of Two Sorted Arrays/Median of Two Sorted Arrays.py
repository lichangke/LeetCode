# @author:leacoder
# @des:  二分查找变式 寻找两个有序数组的中位数
# 什么是中位数：将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素。
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 m < n 便于后续处理
        m, n = len(nums1), len(nums2)
        if m > n: # 如果大于了 交换 nums1 与 nums2
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        # 确保 m < n end

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = int(half_len - i)  # 确保中位数落在左边
            if i < m and nums2[j-1] > nums1[i]:  # 情况二：
                # i 太小
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:  # 情况三：
                # i 太大
                imax = i - 1
            else:  # 情况一：
                # i 满足要求，但有些边界需注意
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:  #  m + n 为奇数
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0   #m + n 为偶数时