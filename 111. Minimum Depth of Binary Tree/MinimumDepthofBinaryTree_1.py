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
            return 0  #Check the input parameter
        else: # BFS
            queue = collections.deque()
            queue.append(root) # Auxiliary queue
            minlevel = 0 # Record level
            while queue:
                levelsize = len(queue)
                minlevel +=1
                
                for i in range(levelsize):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if not node.left and not node.right: # if the node doesn't have left and right subtree, this level is the Minimum Depth
                        return minlevel
                
            
            return minlevel