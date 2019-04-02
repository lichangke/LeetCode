/*
 * @author:leacoder
 * @des: DFS 无优化版 解数独 
 */

class Solution {
    public void solveSudoku(char[][] board) {
        if(board == null || board.length == 0) return;
        solve_DFS(board);
    }
    
    public boolean solve_DFS(char[][] board){
        for ( int y = 0; y < board.length; y++){
            for( int x = 0; x < board[y].length; x++){ //遍历数独每个格子
                if( board[y][x] == '.'){  // 判断是否为空
                    for( char c = '1'; c <= '9'; c++){ // 遍历 1 - 9 数字 是否可行 ,ASCII 中 字符 1 - 9连续
                        if( isValid(board, y, x, c) ){  // 是否可填 c
                            board[y][x] = c; // 填入 然后 DFS 判断 是否正确
                            if(solve_DFS(board)){
                                return true; // ok 成功  正确
                            }
                            else{ //失败  不正确
                                board[y][x] = '.'; //重新标记为空白 不填
                            }          
                        }
                    }
                    return false;  // 1 - 9 没有数能填入  失败
                }
            }
        }
        
        return true;
    }
    public boolean isValid(char[][] board,int row,int col, char c){ // 可填校验
        for(int i = 0; i < 9; i++){
            
            if(board[i][col] !='.' && board[i][col] == c){ // 列检测
                return false; // 检查 每一行  中 col 位是否合法  不能已存在 c
            }
            if(board[row][i] !='.' && board[row][i] == c) {//  行检测
                return false; // 检查 每一列 中 row 位是否合法  不能已存在 c
            }
            if(board[3 * (row/3) + i/3][3 * (col/3) + i%3] != '.' && board[3 * (row/3) + i/3][3 * (col/3) + i%3] == c){
                return false;  // 小 3x3 宫内检测
            }
        }
            
        return true; // 均检测通过 
    }
    
}