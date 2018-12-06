class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        finall=[]
        for i in range(1,numRows):
            row=[None for _ in range(numRows+1)]
            row[0],row[-1]=1,1
            print(row)
            for j in range(1,len(row)-1):
                print(finall[i-1])
            #for j in range(1, len(row)-1):
                row[j]=finall[i-1][j-1]+finall[i-1][j]
                #row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            finall.append(row)
        return row
        # list = [[1],[1,1]]
        # if numRows == 1:
        #     list=[[1]]
        #
        # if numRows == 2:
        #     list=[[1], [1,1]]
        # a = 2
        # while a < numRows:
        #     #print(list[-1])
        #     for i in range(1, len(list[-1])):
        #         tmp = list[-1]
        #
        #         print(tmp)
        #         b=tmp[i]
        #         tmp[i]+=tmp[i-1]
        #         tmp.append(b)
        #         list.append(tmp)


        #     a+=1
        # return list

a=Solution.generate([],5)
print(a)