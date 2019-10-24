# @author:leacoder
# @des: 栈 最小栈

'''
借助辅助栈，栈中存放的是（当前值，当前最小值）
例 依次入栈 -2 0 -3 -4 5
helpstack 从栈顶到下依次为：
(5,-4)
(-4,-4)
(-3,-3)
(0,-2)
(-2,-2)
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.helpstack = [] # (x , curminvalue)

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin: # curMin == None 空栈判断
            curMin = x
        self.helpstack.append((x, curMin))

    def pop(self) -> None:
        return self.helpstack.pop()[0]

    def top(self) -> int:
        if len(self.helpstack) == 0:
            return None
        else:
            return self.helpstack[-1][0]

    def getMin(self) -> int:
        if len(self.helpstack) == 0:
            return None
        else:
            return self.helpstack[-1][1]