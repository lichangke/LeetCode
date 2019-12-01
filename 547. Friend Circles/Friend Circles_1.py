# @author:leacoder
# @des:  DFS 朋友圈

 # 类似于 200. 岛屿数量 

class Solution:
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        
        self.max_M = len(M)
        visited = [0 for _ in range(self.max_M)]
        isCount = 0
        
        # 遍历 M
        for i in range(self.max_M):
            if visited[i] == 0:
                self._dfs(M,visited,i)
                isCount += 1
        return isCount

    # 深度优先
    def _dfs(self, M: List[List[int]], visited: set, i: int)->int:
        for j in range(self.max_M):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self._dfs(M,visited,j)

