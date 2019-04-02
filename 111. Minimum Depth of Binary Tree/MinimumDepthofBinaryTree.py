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
            return 0  #入参校验
        if not root.left: # 判断最小深度 如果没有左子叶，需要看右子叶
            return 1 + self.minDepth(root.right) # +1  因为需要算上root
        if not root.right: # same as root.left
            return 1 + self.minDepth(root.left)
        # divide and conquer
        leftlevel = self.minDepth(root.left)  # 如果 左右子叶都有 深度优先搜索
        rightlevel =  self.minDepth(root.right)
        
        # process subproblem` result
        return 1 + min(leftlevel,rightlevel) # +1  因为需要算上root