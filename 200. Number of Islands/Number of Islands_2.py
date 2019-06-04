# @author:leacoder
# @des:  染色法 + DFS 岛屿的个数


class Solution:
    # 便于 上下左右扩散
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0 # 参数判断
        self.max_x = len(grid);self.max_y = len(grid[0]);self.grid = grid
        self.visited = set() # 不修改原数据
        return sum([self.floodfill_DFS(i,j) for i in range(self.max_x) for j in range(self.max_y)])
    
    # 深度优先 染色
    def floodfill_DFS(self,x,y):
        if not self._is_valid(x,y): # 判断节点是否合法
            return 0
        self.visited.add((x,y)) # 表示节点已经访问过
        for k in range(4):
            self.floodfill_DFS( x + self.dx[k], y + self.dy[k]) # 上下左右扩散
        return 1 # 是岛屿返回1
    
    # 判断节点是否合法
    def _is_valid(self,x,y):
        # max_X max_y边界
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        # 是 '0' 水  或者 已经访问过（处理过）
        if self.grid[x][y] == '0' or ((x,y) in self.visited):
            return False
        return True