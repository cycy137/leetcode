class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)) :
            A[i].reverse()
            for j in range(len(A[i])):
                if A[i-1][j-1]==1:
                    A[i - 1][j - 1]=0
                else:
                    A[i - 1][j - 1]=1

        print( A)


Solution.flipAndInvertImage([],[[1,1,0],[1,0,1],[0,0,0]])