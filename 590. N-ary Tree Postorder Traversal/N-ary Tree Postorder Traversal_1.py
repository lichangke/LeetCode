# @author:leacoder
# @des: 迭代 N叉树的后序遍历

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None:
            return result

        stack = [root]
        # 直接后续遍历比较麻烦，stack.extend(curr.children) 将子节点从左到右入栈，
        # 这样出栈就是从右到左，最后res[::-1] 结果取反
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            stack.extend(curr.children)

        return result[::-1]