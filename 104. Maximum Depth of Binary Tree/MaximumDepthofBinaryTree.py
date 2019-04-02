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
            return 0  #入参校验
        else: # DFS
            leftlevel = self.maxDepth(root.left) #  递归 左子树 得到其深度
            rightlevel = self.maxDepth(root.right) #  递归 右子树 得到其深度
            return 1 + max(leftlevel,rightlevel) # 取最大深度 
        