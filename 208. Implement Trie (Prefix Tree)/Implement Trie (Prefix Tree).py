# @author:leacoder 
# @des:  实现 Trie (前缀树)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.endofword = "end"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            # dict.setdefault(key, default=None) 如果 key 在 字典中，返回对应的值。
            # 如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
            node = node.setdefault(char,{}) 
            
        node[self.endofword] = self.endofword

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            #node = node[char]
            node = node.get(char)
        return self.endofword in node
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            #node = node[char]
            node = node.get(char)
        return True