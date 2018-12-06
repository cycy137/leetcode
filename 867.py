class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # tmp_child=[]
        # tmp=[]
        # outside=len(A )
        # inside=len(A[outside])
        # for i in range (len(A)):
        #     for j in range (len(A[i])):
        #
        #         #while i<len(A)-1:
        #
        #         tmp_child.append(A[j][i])
        #         print(tmp_child)
        #     tmp.append(tmp_child)
        #
        # #return tmp
        # print(tmp)
        return list(zip(*A))
a=Solution.transpose([],[[1,2,3],[4,5,6]])
print(a)