# @author:leacoder
# @des: 递归 N叉树的前序遍历

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.helper(root,result)
        return result

    def helper(self,root,result):
        if not root:
            return
        result.append(root.val)    
        for child in root.children:
            self.helper(child,result)
        