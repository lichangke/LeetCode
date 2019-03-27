#@author:leacoder
#@des:  循环,  二叉搜索树的最近公共祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val<root.val and q.val<root.val: #如果 p q 的值都是小于root的值 那么公共祖先必在其左子树中
                root = root.left
            elif p.val>root.val and q.val>root.val: #如果 p q 的值都是大于root的值 那么公共祖先必在其右子树中
                root = root.right
            else:
                return root