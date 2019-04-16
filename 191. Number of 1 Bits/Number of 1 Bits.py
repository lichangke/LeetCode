# @author:leacoder 
# @des: 32位均判断 位1的个数

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0   #位1 计数
        mask = 1    #
        for i in range(32): #对32位  整数  每位判断
            if n & mask: #判断每个位是否为1
                count += 1
            mask = mask << 1  #左移移位
        return count
            