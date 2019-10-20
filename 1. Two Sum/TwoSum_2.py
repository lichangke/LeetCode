# @author:leacoder
# @des:   字典模拟哈希两遍哈希 两数之和  O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,num in enumerate(nums):
            hashmap[num] = index
        # 哈希建立完成再检测
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)   # 在 hashmap 中找 target - num
            if j is not None and i!=j:  # 能够找到 , 并且 不是 本身
                return [i,j]
