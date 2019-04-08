# @author:leacoder 
# @des: 二分查找 , x 的平方根

class Solution:
    def mySqrt(self, x: int) -> int: 
        if x == 1 or x == 0:
            return x
        left,right,res = 0,x,0
        while left <= right:
            mid = int((left + right)/2)
            if mid * mid > x:
                right = mid - 1
            elif mid *mid < x:
                left = mid + 1
                res = mid
            else:
                return int(mid)  
        return int(res)