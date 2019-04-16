# @author:leacoder 
# @des:  位1的个数

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0   #位1 计数
        while n:
            count += 1
            n = n & (n-1)
        return count