# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @author:leacoder 
# @des:  BFS 广度优先   二叉树的最小深度  时间复杂度 O(n)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0  ##入参校验
        else: # BFS
            queue = collections.deque()
            queue.append(root) # 辅助队列
            minlevel = 0 # 记录层级
            while queue:
                levelsize = len(queue) #记录每层级有多少节点
                minlevel +=1
                
                for i in range(levelsize): #依次处理出这一层级的节点
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left) #对应左子节点
                    if node.right:
                        queue.append(node.right) #对应右子节点
                    if not node.left and not node.right: # 广度优先搜索下来 如果 左右子节点均没有 那么 这个节点所在层级就是最小深度
                        return minlevel
                
            
            return minlevel