# @author:leacoder 
# @des:   递归 括号生成  
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self.fnrecursive(0,0,n,"")
        return self.list
    
   
    #left："("左括号被使用次数  right:")"右括号被使用次数 n:可以被使用括号对数  result：有效括号结果
    def fnrecursive(self,left,right,n,result):
        if left == n and right == n: # 左右括号使用次数均到达n次
            self.list.append(result)
            return
        # 1、要使括号有效 ，那么我们最先放的是 左括号 ，需要满足left < n
        if left < n:
            self.fnrecursive(left+1,right,n,result + "(")
        # 2、要使括号有效 ，右括号使用次数必然不大于左括号，并且 right < n
        if left > right and right < n: 
            self.fnrecursive(left,right+1,n,result + ")")