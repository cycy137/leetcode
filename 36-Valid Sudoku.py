class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            row = set();
            col = set();
            cube = set();
            for j in range(len(board[0])):
                print(row,board[i][j],board[i][j] in row)
                if board[i][j] != "." and board[i][j] in row :return False
                elif board[i][j] != ".": row.add(board[i][j])
                if board[j][i] != "." and board[j][i] in col:return False
                elif board[j][i] != ".": col.add(board[j][i])

                rowIndex = 3 * int(i/3)
                colIndex = 3 * int(i%3)
                if board[rowIndex + int(j/3)][colIndex + int(j%3)]!="." and  board[rowIndex + int(j/3)][colIndex + int(j%3)] in cube :return False
                elif board[rowIndex + int(j/3)][colIndex + int(j%3)]!="." : cube.add(board[rowIndex + int(j/3)][colIndex + int(j%3)])
        return True
a = Solution.isValidSudoku([],[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]])
print(a)