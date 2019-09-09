# @author:leacoder
# @des:   直接反转 整数反转

'''
算法思路：
判断正负，如果为负，先做预处理
循环对当前数x 取10的余数得到 y 以及余数 a，使x = y ；然后将a加入结果res * 10的个位中， res = res * 10 + a。直到 x == 0。

边界情况：
int 取值范围为 [-2^31, 2^31 - 1]，如果循环处理过程中 res 不在这个范围，立即返回0

'''

class Solution:
    def reverse(self, x: int) -> int:
    	res = 0 
    	if x < 0:
    		y  = -x 
    		checknum = 2**31  # x 为负 取反后其最大值为 2^31
    	else:
            y  =  x 
            checknum = 2**31 - 1  # -

    	while y != 0:
    		res = res * 10 + y % 10
    		if res > checknum:
    			return 0
    		y = y // 10

    	return res if x > 0 else -res