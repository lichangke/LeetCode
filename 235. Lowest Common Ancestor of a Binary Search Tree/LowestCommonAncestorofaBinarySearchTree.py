#@author:leacoder
#@des:  递归,  二叉搜索树的最近公共祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val and q.val<root.val: #如果 p q 的值都是小于root的值 那么 需要在二叉搜索树 左子树中找
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val: #如果 p q 的值都是大于root的值 那么 需要在二叉搜索树 右子树中找
            return self.lowestCommonAncestor(root.right,p,q)
        return root  #其他情况  一个比root 大 一个比root小 那么 root必然为其公共祖先