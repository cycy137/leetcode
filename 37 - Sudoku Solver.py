class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0: return
        def dfs(self,board):

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        for h in range(1,10):
                            if solve([],board,i,j,h):
                                board[i][j] = str(h)
                                if "." not in board[-1]:return True
                                if dfs(self,board):return True

                                else:
                                  #  print(board[8])
                                    board[i][j] ="."

                        return False
        def solve(self,board,row,col,num):
            num = str(num)
            for i in range(0,9):
                if board[i][col] != "." and board[i][col]==num:return False
                if board[row][i] != "." and board[row][i] == num:return False
                #print([3*(row//3) + (i//3),3*(col//3) + (i%3)])
                if board[3*(row//3) + (i//3)][3*(col//3) + (i%3)] != "." and board[3*(row//3) + (i//3)][3*(col//3) + (i%3)]==num :return False
            return True
        dfs([], board)
        print(board)
a = Solution.solveSudoku([],[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
print(a)