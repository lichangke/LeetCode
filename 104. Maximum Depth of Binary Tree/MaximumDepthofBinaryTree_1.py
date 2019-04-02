# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @author:leacoder 
# @des:  BFS 广度优先  二叉树的最大深度  时间复杂度 O(n)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0  #入参校验
        else: # BFS
            queue = collections.deque()
            queue.append(root) # 辅助队列
            maxlevel = 0 #层级记录
            while queue:
                levelsize = len(queue) #
                for i in range(levelsize): 
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                maxlevel +=1 # 广度优先搜索 每层搜完 层级+1
            
            return maxlevel