# @author:leacoder
# @des:  并查集 朋友圈

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        n = len(M)

        # 创建并查集
        p = [i for i in range(n)]

        # 合并
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.union(p,i,j)
        
        # 有多少不同的parent
        # return len(set([self.parent(p,i) for i in range(n)]))
        findCircle = set()
        for i in range(n):
            findCircle.add(self.parent(p,i))
        return len(findCircle)


    def union(self, p, i, j): 
        p1 = self.parent(p,i) # 找 i j 各自的领头元素 
        p2 = self.parent(p,j)
        p[p2] = p1
    
    def parent(self, p, i):  # 找 i 的 领头元素
        root = i
        while p[root] != root: # parent 结点不是自己
            root = p[root] # 不断向上 直到直到领头元素
        # 路径压缩 将i到root沿途所有结点指向root
        while p[i] != root:
            # x = i; i = p[i]; p[x] = root
            i,p[i] = p[i],root
        return root