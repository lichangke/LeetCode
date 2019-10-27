# @author:leacoder
# @des: 迭代 + 借助栈 二叉树的中序遍历

'''
先找重复处理单元:
二叉树左右两子节点处理，以及根节点处理
前序遍历： 根结点 ---> 左子树 ---> 右子树
中序遍历： 左子树---> 根结点 ---> 右子树
后序遍历： 左子树 ---> 右子树 ---> 根结点
以上为深度遍历
也可以按层次遍历：只需按层次遍历即可

迭代终止条件：
节点遍历完

迭代前处理
迭代处理
root 以及 left 依次入栈到叶子节点
处理当前，然后处理 right

迭代后处理

'''


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right   # 处理 right
