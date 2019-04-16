# @author:leacoder 
# @des: Trie (前缀树，字典树) + DFS  单词搜索 II
# 将words存入 Trie 中，然后将board 中的字母按顺序依次与 Trie 中字母比较 


dx = [ 0, 0,-1, 1]
dy = [-1, 1, 0, 0,]
# 在board 中以当前位置（x0,y0） 上下左右的偏移量 ,上偏移(x0,y0-1) 下偏移（x0,y0+1） 左偏移（x0+1,y0） 右偏移（x0-1,y0）

class Trie: #辅助 Trie
    def __init__(self):
        self.root = {}
        self.endofword = "end"

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # dict.setdefault(key, default=None) 如果 key 在 字典中，返回对应的值。
            # 如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
            node = node.setdefault(char,{})      
        node[self.endofword] = self.endofword

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        if not words: return []
        self.result = set()
        self.myTrie = Trie()
        
        for word in words:
            self.myTrie.insert(word)
            
        self.row ,self.col = len(board), len(board[0])  # 行 y   列 x
        
        for i in range(self.row): 
            for j in range(self.col): #board中每一个字符开始 深度优先搜索
                if board[i][j] in self.myTrie.root: # myTrie 中有前缀 board[i][j]
                    self._dfs(board,i,j,"",self.myTrie.root)
                    
        return list(self.result)
    
    # def
    def _dfs(self, board, i, j, cur_word, cur_dict):
        
        cur_word += board[i][j]  #board[i][j] 必然已经搜索到 累加字符  
        cur_dict = cur_dict[board[i][j]] # Trie树的下一层 某个word的下一字符
        
        if self.myTrie.endofword in cur_dict: # 是否已经探寻到Trie最后 也就是words中某个word 被找到
            self.result.add(cur_word)
        
        tmp,board[i][j] = board[i][j],"#"  #暂存 board[i][j]  用“#” 标记是否被访问过了   用于下面偏移
        
        for k in range(4): # 上下左右偏移 
            y, x = i + dy[k], j + dx[k]
            # 上下左右偏移 必须在row和col之内，偏移后的字符 board[y][x]没有被访问处理过，并且 偏移后的字符在Trie树的下一层有
            if 0 <= x < self.col and 0 <= y < self.row: # 注意范围
                if board[y][x] !="#" and board[y][x] in cur_dict:
                    self._dfs(board,y,x,cur_word,cur_dict)  # 深度优先继续搜索
        
        board[i][j] = tmp #循环结束 恢复以前数据 （board[i][j]之前被设置为"#"标记是否被访问过了）
            
            
            
            
            
            