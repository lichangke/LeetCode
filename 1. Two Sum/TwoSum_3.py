# @author:leacoder
# @des:   字典模拟哈希一遍哈希 两数之和  O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        # 边建立遍检测已建立部分是否存在， 有就立即返回
        for i,num in enumerate(nums):
            # hashmap[num] = i # 先存会有问题 
            j = hashmap.get(target - num)   # 在 hashmap 中找 target - num
            if j is not None and i!=j:  # 能够找到 , 并且 不是 本身
                return [i,j]
            hashmap[num] = i # 解决list中有重复值或target-num=num的情况 例如 [3,3] 6