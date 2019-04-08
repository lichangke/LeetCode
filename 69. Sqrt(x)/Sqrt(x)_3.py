# @author:leacoder 
# @des: 神秘的常数 0x5f3759df 0x5f375a86, x 的平方根
# 参看 http://www.cnblogs.com/pkuoliver/archive/2010/10/06/1844725.html
# 参看 https://www.beyond3d.com/content/articles/8/

class Solution:
    def mySqrt(self, x: int) -> int: 
        if x <= 1:
            return x
        r = x
        r = 0x5f3759df - (r >> 1)
        while r * r > x:
            r = int((r + x / r) /2)
        return int(r)