# @author:leacoder
# @des:  染色法 + BFS 岛屿的个数


class Solution:
    # 便于 上下左右扩散
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0 # 参数判断
        self.max_x = len(grid);self.max_y = len(grid[0]);self.grid = grid
        self.visited = set() # 不修改原数据
        return sum([self.floodfill_BFS(i,j) for i in range(self.max_x) for j in range(self.max_y)])
    
    # 广度优先 染色
    def floodfill_BFS(self,x,y):
        if not self._is_valid(x,y): # 判断节点是否合法
            return 0
        self.visited.add((x,y)) # 标记节点已经访问过
        queue = collections.deque() # 队列
        queue.append((x,y))
        while queue: # 不为空一直循环
            cur_x, cur_y = queue.popleft() # 从队列左端取数据
            
            for i in range(4):
                new_x, new_y = cur_x + self.dx[i], cur_y + self.dy[i] #上下左右扩散
                if self._is_valid(new_x, new_y): # 扩散后的数据是否合法
                    self.visited.add((new_x, new_y)) # 合法标记节点已经访问过
                    queue.append((new_x, new_y)) # 从右端加入队列
        return 1
    
    # 判断节点是否合法
    def _is_valid(self,x,y):
        # max_X max_y边界
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        # 是 '0' 水  或者 已经访问过（处理过）
        if self.grid[x][y] == '0' or ((x,y) in self.visited):
            return False
        return True