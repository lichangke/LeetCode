# @author:leacoder
# @des:   双指针  三数之和

'''

双指针法铺垫： 先将给定 nums 排序，复杂度为 O(NlogN)。
双指针法思路： 固定 3个指针中最左（最小）数字的指针 k，双指针 i，j 分设在数组索引 (k, len(nums)) 两端，
通过双指针交替向中间移动，记录对于每个固定指针 k 的所有满足 nums[k] + nums[i] + nums[j] == 0 的 i,j 组合：

1、当 nums[k] > 0 时直接break跳出：因为 nums[j] >= nums[i] >= nums[k] > 0，即 3个数字都大于 0 ，在此固定指针 k 之后不可能再找到结果了。

2、当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：因为已经将 nums[k - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。

3、i，j 分设在数组索引 (k, len(nums)) 两端，当i < j时循环计算s = nums[k] + nums[i] + nums[j]，并按照以下规则执行双指针移动：
    当s < 0时，i += 1并跳过所有重复的nums[i]；
    当s > 0时，j -= 1并跳过所有重复的nums[j]；
    当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        nums.sort()     # 排序后 nums有序 递增
        count = len(nums)
        for k in range(count-2):    # 固定 3个指针中最左（最小）数字的指针 k
            if nums[k] > 0:
                break       # 1. nums[j] >= nums[i] >= nums[k] > 0，即 3个数字都大于 0
            if k > 0 and nums[k] == nums[k - 1]:
                continue    # 2. 即跳过此元素nums[k]：因为已经将 nums[k - 1] 的所有组合加入到结果中
            i, j= k+1, count-1  # 初始化 i j
            while i < j:    # i 只能递增  j 只能递减  向中间移动
                s = nums[k] + nums[i] + nums[j]
                if s < 0:   # nums[i] + nums[j] 过小 增大 i
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1  # 跳过所有重复的nums[i]；
                elif s > 0:     # nums[i] + nums[j] 过大 减小 j
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1  # 跳过所有重复的nums[j]；
                else:
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1  # 跳过所有重复的nums[i]；
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1  # 跳过所有重复的nums[j]；

        return result
                