#@author:leacoder
#@des:  递归,  验证二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min = max = None
        return self.isValid(root,min,max)
    
    def isValid(self,root,min,max):
        if root is None:
            return True
        # 当前root节点值 必须在 min 和 max之间
        if min is not None and root.val <=min:
            return False
        if max is not None and root.val >=max:
            return False
        # 分别递归检测   root的左子树（min下界不关心，其上界必须是root的值） 与 root右子树（max上界不关心，其下界必须是root的值）
        if self.isValid(root.left,min,root.val) and self.isValid(root.right,root.val,max):
            return True
        else:
            return False
    
    