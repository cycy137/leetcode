class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        res = []
        mid = [["." for _ in range(n)] for _ in range(n)]


        def helper(col):
            if col ==n  :  #swith gurantee list to string and append it to res
                print(mid)
                tmp = []
                for i in mid:
                    a = "".join(i)
                    tmp.append(a)

                res.append(tmp)

            for row in range(n):
                if   valid(row,col) :
                    mid[row][col] = "Q"
                    helper(col+1)
                    mid[row][col] = "."
        def valid( row, col):

            for i in range(n):
                if col > 3: return False
                print(i,col)
                if mid[i][col] == "Q": return False
                if mid[row][i] == "Q": return False

                for j in range(n):
                    if (i - j) == (row-col):
                        if mid[i][j] == "Q": return False
                    if (i + j) == (row+col):
                        if mid[i][j] == "Q": return False
            return True
        # def valid( row, col):
        #     for c in range(col):
        #         if mid[row][c] == "Q":
        #             return False
        #     rup = row - 1
        #     rdown = row + 1
        #     c = col - 1
        #     while c >= 0:
        #         if rup >= 0:
        #             if mid[rup][c] == "Q":
        #                 return False
        #         if rdown < n:
        #             if mid[rdown][c] == "Q":
        #                 return False
        #         rup -= 1
        #         rdown += 1
        #         c -= 1
        #     return True

        helper(0)
        print(res)
        return res
a= Solution.solveNQueens([],4)
print(a)
#
# fin = []
#         mid = []
#         res = ["." * n for _ in range(n)]
#         print(res)
#         def valid(res, row, col):
#             for i in range(n):
#                 if res[i][col] == "Q": return False
#                 if res[row][i] == "Q": return False
#
#                 for j in range(n):
#                     if (i - j) == (row-col):
#                         if res[i][j] == "Q": return False
#                     if (i + j) == (row+col):
#                         if res[i][j] == "Q": return False
#             return True
#         def helper(res,  fin,n):
#             if len(mid) == n:
#                 fin.append(res)
#                 return
#             for i in range(n):
#                 for j in range(n):
#
#                     res[i][j].replace(".","Q")
#
#                     if valid(res, i, j):
#                         return True
#                     else:
#                         res[i][j].replace("Q",".")
#
#
#
#         helper(res,fin,n)
#         return fin