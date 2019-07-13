# @author:leacoder 
# @des: 借助小顶堆(heapq---堆队列算法也称为优先队列算法) ,  数据流中的第K大元素

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # heapq.nlargest(n, iterable, key=None) 返回一个列表，其中包含iterable定义的数据集中的n个最大元素。
        self.k_heap = heapq.nlargest(k, nums)
        # heapq.heapify(x) 将list x 转换成堆，原地，线性时间内
        heapq.heapify(self.k_heap)
        self.k = k
        
    def add(self, val: int) -> int:
        if len(self.k_heap) < self.k:
            # 直接加入
            heapq.heappush(self.k_heap,val)
        else:
            # 先加入再弹出最小，维护元素为k个
            # heapq.heappushpop(heap, item) 将 item 放入堆中，然后弹出并返回 heap 的最小元素。
            heapq.heappushpop(self.k_heap,val)
        # 最小的元素总是在根结点：heap[0],由于维护的元素个数为k，那么就为第k大元素
        return self.k_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
