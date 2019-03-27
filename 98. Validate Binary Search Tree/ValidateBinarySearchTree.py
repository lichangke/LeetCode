#@author:leacoder
#@des:  中序遍历  验证二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorderlist = self.inorder(root) #中序遍历后 如果是二叉搜索树 那么 结果必然是递增有序的 
        return inorderlist == list(sorted(set(inorderlist))) #set 集合用于去重  有重复的数那么必然不是二叉搜索树
        
    def inorder(self,root): #中序遍历 形成 左 根 右形式
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    
    
    '''
    sort() 对list本身进行排序,改变list的值。sort()只能对list排序。
    sorted() 产生一个新的list，不改变list的值。sorted()可以对iterable对象排序
    集合（set）是一个无序的不重复元素序列。
    可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。