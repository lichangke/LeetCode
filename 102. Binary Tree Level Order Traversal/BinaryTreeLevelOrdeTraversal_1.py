
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @author:leacoder 
# @des:  DFS 深度优先  二叉树的层次遍历  时间复杂度 O(n)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.result = []
        self.dfs(root,0) #深度优先搜索，每次传入层级 便于将每层级节点存放起来
        return self.result
    def dfs(self,node,level):
        if not node: return []
        
        if len(self.result) < level +1: #结果按这种方式 [ [0层数据],[1层数据] ,... ,[n层数据] ] 存储
            self.result.append([])  # 如果结果长度小于了层级 表明 需要新加一层级数据存放[]
            
        self.result[level].append(node.val) #将当前节点 按层级 存放入对应结果中
        
        self.dfs(node.left,level+1)  #递归深度优先查找  level 每层加1
        self.dfs(node.right,level+1)  #递归深度优先查找  level 每层加1