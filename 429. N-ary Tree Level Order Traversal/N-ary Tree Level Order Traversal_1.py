# @author:leacoder
# @des: 递归 N叉树的层序遍历


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        level = 0
        self.helper(level,root,result)
        return result

    def helper(self,level,root,result):
        if not root:
            return 
        # 判断是否是新的一层
        if level>=len(result):
            result.append([])
        result[level].append(root.val)  # 将结果加入对应层的结果中

        for item in root.children:
            self.helper(level+1,item,result)
        





