# @author:leacoder
# @des: 递归 N叉树的后序遍历


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.helper(root,result)
        return result

    def helper(self,root,result):
        if not root:
            return
        for child in root.children:
            self.helper(child,result)
        result.append(root.val)
