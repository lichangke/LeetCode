# @author:leacoder 
# @des:   递归 括号生成  
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self.fnrecursive(0,0,n,"")
        return self.list
    
    # left :the count "(" has been used , right :the count "）" has been used
    # n the pairs of parentheses , result :   one combinations of well-formed parentheses
    def fnrecursive(self,left,right,n,result):
        if left == n and right == n:
            self.list.append(result)
            return
        # first ,we should put "(" .  if not the combination is bad-formed parentheses
        if left < n:
            self.fnrecursive(left+1,right,n,result + "(")
        # if left > right and right < n ,then ,we put ")"
        # if left < right, the combination is bad-formed parentheses
        if left > right and right < n: 
            self.fnrecursive(left,right+1,n,result + ")")