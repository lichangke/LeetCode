# @author:leacoder 
# @des: 牛顿迭代 , x 的平方根
# 参看 https://www.cnblogs.com/qlky/p/7735145.html

class Solution:
    def mySqrt(self, x: int) -> int: 
        if x <= 1:
            return x
        r = x
        while r * r > x:
            r = int((r + x / r) /2) 
        return r