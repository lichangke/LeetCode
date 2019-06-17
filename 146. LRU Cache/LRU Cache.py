# @author:leacoder
# @des:   LRU(最近最少使用) 缓存机制
# OrderedDict 参看 https://docs.python.org/3/library/collections.html#collections.OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()    # OrderedDict 记住了字典元素的添加顺序
        self.remain = capacity # 容量 大小

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v # 被获取 刷新最近使用
        return v
    
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key) # 如果字典中有先弹出 再加入
        else: # 没有
            if self.remain > 0: # 字典未满
                self.remain -= 1 # 剩余容量 -1
            else: #  字典已满 弹出最近最少使用的，最老的元素
                self.dic.popitem(last = False)
                '''
                popitem(last=True)
                The popitem() method for ordered dictionaries returns and removes a (key, value) pair. 
                The pairs are returned in LIFO order if last is true or FIFO order if false.
                '''
        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)