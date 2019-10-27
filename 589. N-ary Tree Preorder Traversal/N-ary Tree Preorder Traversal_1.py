# @author:leacoder
# @des: 迭代 N叉树的前序遍历

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None:
            return result

        stack = [root]
        # 直接前续遍历即可
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.children:   #如果该元素有子节点children 则反转加入到 stack 里(因为是前序遍历)
                for item in curr.children[::-1]:
                    stack.append(item)
        return result