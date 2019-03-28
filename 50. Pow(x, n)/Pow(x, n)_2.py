# @author:leacoder
# @des:  递归  Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: #递归终止条件
            return 1
        if n<0: #n<0的情况
            return 1/self.myPow(x,-n)
        if n%2 == 0: # n为偶数
            return self.myPow(x*x,n/2) # x(n/2) * x(n/2) = (x * x)(n/2)
        else:#n为奇数
            return x*self.myPow(x,n-1) # x * x((n-1)/2) * x((n-1)/2) = x * (x*x)((n-1)/2) = x* x(n-1)
            # return x*self.myPow(x*x,(n-1)/2)