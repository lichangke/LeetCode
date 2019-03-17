#@author:leacoder
#@des: 用栈实现队列
class MyQueue:

    def __init__(self):
        self.inputstack = []
        self.outputstack = []
        

    def push(self, x: int) -> None:
        self.inputstack.append(x)
        

    def pop(self) -> int:
        if 0!=len(self.outputstack):
            return self.outputstack.pop()
        else:
            while 0!=len(self.inputstack):     
                self.outputstack.append(self.inputstack.pop())      
            return self.outputstack.pop()        

    def peek(self) -> int:
        if 0!=len(self.outputstack):
            return self.outputstack[-1]
        else:
            while 0!=len(self.inputstack):
                self.outputstack.append(self.inputstack.pop())
            return self.outputstack[-1]

    def empty(self) -> bool:
        return 0==len(self.inputstack) and 0==len(self.outputstack)
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()