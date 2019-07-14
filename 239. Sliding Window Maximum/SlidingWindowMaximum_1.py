# @author:leacoder
# @des:  双端队列 滑动窗口最大值

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        length = len(nums)
        window ,result = [],[]  #window 存在窗口中的数  result用于存最后的结果
        for i, numx in enumerate(nums):
            if i>=k-1: # k个元素开始 维护  window
                window.append(numx) # 加入新元素
                result.append(max(window))  # 取出最大值
                window.pop(0) # 删除下一轮要离开的元素
            else: # k - 1元素直接加入 window
                window.append(numx)
        
        return result 