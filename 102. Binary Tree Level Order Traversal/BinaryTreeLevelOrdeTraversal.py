
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# @author:leacoder 
# @des:  BFS 广度优先  二叉树的层次遍历  时间复杂度 O(n)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []  #输入参数校验
        result = []
        
        # deque 可参考 https://docs.python.org/3/library/collections.html#collections.deque
        queue = collections.deque()  #辅助队列  
        queue.append(root)
        # visited = set(root) #用于存放是否访问过 这样可以访问图
        
        while queue:
            level_node_count = len(queue) #获取当前层级 节点个数 
            currentlevel_nodes = [] #用于存放当前层级所有节点
            
            for i in range(level_node_count): #根据当前层级节点个数  循环遍历当前层级所有node
                node = queue.popleft()  #从左移除 节点
                currentlevel_nodes.append(node.val) #存储当前节点
                #由于循环之前已经获取 当前层级节点个数 ,循环按当前层级节点个数遍历并移除当前节点   
                #故下一层级节点直接加入 当循环结束 queue 存放的就只有下一层级所有节点 
                if node.left:#下一层 当前节点左子节点 不为空
                    queue.append(node.left) #加入  queue 
                if node.right:#下一层 当前节点右子节点 不为空
                    queue.append(node.right)
                    
            result.append(currentlevel_nodes)
            
        return result