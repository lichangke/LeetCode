# @author:leacoder 
# @des:   加一

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(length-1, -1, -1):
            num = digits[i]
            if num < 9:
                digits [i] = num + 1
                return digits
            else:
                digits [i] = 0
                if i == 0:
                    digits =  [1] + digits
        return digits