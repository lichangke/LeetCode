# @author:leacoder
# @des:  动态规划 最小路径和

'''
可以不用额外存储空间，直接在原数组上存储dp

'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        max_y = len(grid)
        max_x = len(grid[0])
        for i in range(max_y):
            for j in range(max_x):
                if i == 0 and j == 0: 
                    continue
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]
        return grid[max_y-1][max_x-1]