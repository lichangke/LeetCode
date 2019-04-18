# @author:leacoder 
# @des:  DFS 深度优先  N皇后II

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1 : return []  #
        self.count = 0
        shu = [] # 竖方向是否被攻击
        pie = [] # 撇方向是否被攻击  x y 坐标之和固定 x + y
        na = []  # 捺方向是否被攻击  x y 坐标之差固定 x - y
        
        self.DFS(n,shu,pie,na)
        
        return self.count
    
    def DFS(self,n,shu,pie,na): #深度优先搜索 
        p = len(shu) #  从 1 -> n
        if p == n :
            self.count += 1 #每层有且只能放一个
            return 
        for q in range(n): # 看成 x  每层枚举可能的 x
            if q not in shu and p - q not in na and p + q not in pie: #这一层存在可能位置，向下层搜索
                self.DFS(n,shu+[q],pie+[p+q],na+[p-q])  #深度优先搜索  将被攻击的 坐标记录下来 
        
        