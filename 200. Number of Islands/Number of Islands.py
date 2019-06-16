# @author:leacoder
# @des:  并查集 岛屿的个数

'''
1、初始化：将所有'1'（陆地）节点 root 指向自己
2、遍历：遍历所有节点，为1 相邻节点合并，为0 不管
3、遍历查询总共有多少root（可在2统计）
'''

class UnionFind(object):
    def __init__(self,grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1]*(m*n)
        self.rank = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # 为 1 时 count + 1
                    self.parent[i*n+j] = i*n+j  # 初始化：将所有'1'（陆地）节点 root 指向自己
                    self.count +=1
    
    def find(self,i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # 如果parent不是自己，继续向上查找，找到属于哪个集合
        return self.parent[i] # 如果parent是自己,返回这个值
    
    def union(self,x,y):
        rootx = self.find(x) # 找 x 的 parent
        rooty = self.find(y) # 找 y 的 parent
        if rootx != rooty: # 不同 不在一个集合中
            ''' 如果不管rank 
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            '''
            self.parent[rootx] = rooty # 将两个 合为 同一个 集合中
            self.count -=1  # 每次union  count-1
            

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):  # 遍历：遍历所有节点，为1 相邻节点合并，为0 不管
                if grid[i][j] == '0':
                    continue
                for d in directions: # 上下左右 扩散
                    nr,nc = i + d[0],j+d[1]                
                    if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == '1': # 坐标合法 并且 为 1
                        uf.union(i*n+j,nr*n+nc) # 为1 相邻节点合并到同一集合
        # 遍历查询总共有多少root（可在2统计）
        return uf.count # 由于 union 中 被合并为同一集合 count -1 ，最后就剩 唯一的了 