#@author:leacoder
#@des:  中序遍历 优化  验证二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        return self.helper(root)
    
    def helper(self,root): #中序遍历 但是不全返回， 比较前节点是否比后节点小 小:二叉搜索树 大：非二叉搜索树
        if root is None:
            return True
        if not self.helper(root.left): #先判断左子树
            return False
        #前节点 与 后节点比  
        if self.prev and self.prev.val >= root.val:  #左子树:left 与root比    右子树：root与right比
            return False
        
        self.prev = root  #右子树将prev 设为 root
        #程序向后走（判断右叶子） 将前节点（root）与后节点（right）比较
        return self.helper(root.right) #再判断右子树
        
        '''
        对每个  left root right 判断 是否  left <root< right
        '''