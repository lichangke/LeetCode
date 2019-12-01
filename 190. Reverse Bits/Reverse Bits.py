# @author:leacoder 
# @des: 位运算  颠倒二进制位

class Solution:
    def reverseBits(self, n: int) -> int:
        result , MASK = 0, 1
        for i in range(32):
            if n & MASK:    # 取出 MASK 的 那一位, 如果是 1 
                result |= 1 << (31 - i)  # 第 i 位
            MASK = MASK << 1 # 依次右移    移动31次
        return result