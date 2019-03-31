# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @author:leacoder 
# @des:  DFS 深度优先  二叉树的最大深度  时间复杂度 O(n)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0  #Check the input parameter
        else: # DFS
            leftlevel = self.maxDepth(root.left) #  Recursive  Left subtree
            rightlevel = self.maxDepth(root.right) #  Recursive  Right subtree
            return 1 + max(leftlevel,rightlevel) # +1 because of the root
        