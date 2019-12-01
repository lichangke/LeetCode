# @author:leacoder 
# @des: 利用X & (X-1) 位1的个数


# X & (X-1) 清零最低位的 1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0   #位1 计数
        while n:
            count += 1
            n = n & (n-1)   # X & (X-1) 清零最低位的 1
        return count