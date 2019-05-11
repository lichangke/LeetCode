#@author:leacoder
#@des:  动态规划  编辑距离

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        '''
        动态规划 
        step1: 状态  
        首先只定义一维 DP[i] 不能有效简化问题的处理
        使用 二维 DP[i][j]，表示 word1 的 i 个字母 与 word2 的 第 j 个字母 相同 需要的操作步骤数
        将最对 word1 处理 转化为 对 word1 和 word2 均处理
        word1 插入一个字符   DP[i-1][j] + 1 ->  DP[i][j]
        word1 删除一个字符 = word2 插入一个字符  DP[i][j-1] + 1 -> DP[i][j]
        word1 替换一个字符 = word1 word2 都替换一个字符 DP[i-1][j-1] + 1 -> DP[i][j]
        step2: 动态方程
        DP[i][j]  A、 word1 的 i 个字母 与 word2 的 第 j 个字母 相同
                     DP[i][j] =  DP[i-1][j-1]  #不操作
                  B、不相同,需要进行 插入 删除 或者 替换操作
                     DP[i][j]  =  min(DP[i-1][j] + 1,DP[i][j-1] + 1,DP[i-1][j-1]+1)
        
        '''
        DP = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        # 初始
        for i in range(len1+1):
            DP[i][0] = i
        for j in range(len2+1):
            DP[0][j] = j
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i - 1] == word2[j -1]:
                    DP[i][j] =  DP[i-1][j-1]
                else:
                    DP[i][j]  =  min(DP[i-1][j] + 1,DP[i][j-1] + 1,DP[i-1][j-1]+1)
        return DP[len1][len2]