# @author:leacoder
# @des:   字典加速  三数之和
'''
在暴力法的基础上用hash表加速，O(n^2)
使用字典存储所有数据
有问题
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = len(nums)
        result = list()
        dict_data = dict()

        for index in range(count):  # 构建辅助字典
            dict_data[nums[index]] = dict_data.get(nums[index],0)+1

        if 0 in dict_data and dict_data[0] >= 3:
            result.append([0, 0, 0])

        neg = list(filter(lambda x: x < 0, dict_data))
        pos = list(filter(lambda x: x >= 0, dict_data))

        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in dict_data:
                    if dif in (i, j) and dict_data[dif] >= 2:
                        result.append([i, j, dif])
                    if dif < i or dif > j:
                        result.append([i, j, dif])

        return result
