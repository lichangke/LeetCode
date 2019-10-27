# @author:leacoder
# @des: 递归 二叉树的前序遍历


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root,result)
        return result

    def helper(self,root,result):
        if not root:
            return
        result.append(root.val)
        self.helper(root.left,result)
        self.helper(root.right,result)