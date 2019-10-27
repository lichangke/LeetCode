# @author:leacoder
# @des: 迭代 + 队列 N叉树的层序遍历


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return
        queue = [root]  # #初始化一个 队列  root
        result = []

        while queue:    
            nodes = []
            childval = []
            for item in queue:  # 依次取出 队列 中数据
                childval.append(item.val)   # 取值
                if item.children:   # 子节点加入 nodes 最后赋值给queue
                    nodes.extend(item.children)
            result.append(childval)
            queue = nodes
        return result




