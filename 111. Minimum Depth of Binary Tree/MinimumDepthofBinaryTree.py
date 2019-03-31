# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @author:leacoder 
# @des:  DFS 深度优先 二叉树的最小深度  时间复杂度 O(n)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0  #Check the input parameter
        if not root.left: # if not have left subtree,check the right subtree
            return 1 + self.minDepth(root.right) # +1 because of the root
        if not root.right: # same as root.left
            return 1 + self.minDepth(root.left)
        # divide and conquer
        leftlevel = self.minDepth(root.left)  # DFS 
        rightlevel =  self.minDepth(root.right)
        
        # process subproblem` result
        return 1 + min(leftlevel,rightlevel) # +1 because of the root