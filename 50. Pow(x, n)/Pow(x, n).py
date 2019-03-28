# @author:leacoder
# @des:  非递归  Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        pow = 1
        while n:
            if n&1: # n 为奇数
                pow *= x
            
            x *=x #偶数   x = x*x  n=n>>1 (右移1 n减半)   即为 x(n) = (x*x)(n/2)
            n >>=1
            
        return pow