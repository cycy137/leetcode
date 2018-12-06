class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        print("sdf")
        result = []

        board = [["." for x in range(n)] for x in range(n)]
        print(board)



        def solve( col):
            if col == n:
                solution = []
                for row in board:
                    string = ""
                    for char in row:
                        string += char
                    solution.append(string)
                result.append(solution)
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    solve(col + 1)
                    board[row][col] = "."

        def isSafe( row, col):
            for c in range(col):
                if board[row][c] == "Q":
                    return False
            rup = row - 1
            rdown = row + 1
            c = col - 1
            while c >= 0:
                if rup >= 0:
                    if board[rup][c] == "Q":
                        return False
                if rdown < n:
                    if board[rdown][c] == "Q":
                        return False
                rup -= 1
                rdown += 1
                c -= 1
            return True

        solve(0)
        print(result)
        return result
a = Solution.solveNQueens([],4)
print(a)

