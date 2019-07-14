# @author:leacoder
# @des:  双端队列(优化) 滑动窗口最大值

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        window ,result = [],[]  #window 存在窗口中的数的 下标  result用于存最后的结果
        
        for i, numx in enumerate(nums):
            """
            1.判断元素是否超出滑动窗口范围
            i > k 说明滑动窗口不为空，window[0] < i - k说明最大元素超出了窗口，这时候必须舍弃
            队首元素：window.pop(0)
            """
            if i>=k and window[0]<=i-k: #新数据来时每次将window最左边的pop掉window[0]放的是最大而不是最左边界所以需要判断
                window.pop(0) #不满足 window内条件 
            while window and nums[window[-1]]<=numx: #维护window   保持k的范围内window最大数始终在windowp[0]
                window.pop()  #window中如果有比新进numx小的 pop掉(我们要的是窗口内最大)  
            window.append(i) 
            #将新进numx 下标加入window  window中最大数 始终是window[0] 
            #因为上方while循环已经保证在append新进数时 window中要么为空，新进入数最大 
            #要么比新进数入小的已pop掉留下比新进入数大的数放在头部
            if i>=k-1: #下标从0开始 顾 i=k-1时 window中已处理过k个数了
                result.append(nums[window[0]])
        return result
    
'''
巧妙运用了window大小固定，并且 新进入数 如果比之前window中已有数都大的话，那么之前的数永远不可能是我们需要的数（滑动窗口最大值） 
1 3 -1 -3 5 3 6 7 为nums  k=3为例

假设已到新数进入前 窗口为 1 [3 -1 -3] 5 3 6 7, 现在新数 5 下标为四进入，按着上面代码逻辑
1、pop掉窗口最最左边数 3 下标为一 被pop
2、此时window中为[ -1 -3 ]的下标，循环比较 新数 5 大于 -1 -3 顾pop掉。此时window为空 跳出循环
3、将新数 5下标为四 append入window (存放下标) 此时window为[四]    1 3 [-1 -3 5] 3 6 7
4、这时窗口中最大值 为window[0]为下标的数
5、新进数3下标五 进入，-1 已不在window内了不需pop，window中只有5下标为四 不需要pop任何数据，将3 下标五append入window(存放下标) 此时window为[四 五]   1 3 -1 []-3 5 3] 6 7 窗口中最大值 依旧为window[0]为下标的数

'''