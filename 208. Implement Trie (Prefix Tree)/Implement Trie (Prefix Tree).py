# @author:leacoder 
# @des:  实现 Trie (前缀树)
class Trie:

    def __init__(self):
        self.root = {}  # 根节点
        self.endofword = "#"    # 标识是否是一个完整的单词
        

    def insert(self, word: str) -> None:
        # 插入操作
        node = self.root    # 根节点
        for char in word:   # 遍历单词 word 中每个字符
            node = node.setdefault(char,{}) # 字典形式依次将字符保存到树的每一层中
            # dict.setdefault(key, default=None) 如果 key 在 字典中，返回对应的值。
            # 如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
        node[self.endofword] = self.endofword   # 完整单词标识
        

    def search(self, word: str) -> bool:
        # 查找操作
        node = self.root
        for char in word:   # 遍历单词 word 中每个字符
            if char not in node:    # 未找到
                return False
            node = node.get(char)   # 找到进入下一结点
        return self.endofword in node # 是否为完整的单词
        

    def startsWith(self, prefix: str) -> bool:
        # 字典树中是否有以 prefix 为前缀的单词
        node = self.root
        for char in prefix: # 遍历 前缀 prefix
            if char not in node:
                return False
            node = node.get(char) 
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)