class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # finall[1]
        # for _ in range(rowIndex)
        #     finall=[x+y for x,y in zip]

        finall = [[1], [1, 1]]
        nums=2
        while len(finall) <= rowIndex:
            row = []
            for i in range(nums + 1):
                if i == 0 or i == nums:
                    row.append(1)
                else:
                    print(nums + 1,i,finall[nums - 1][i - 1] + finall[nums - 1][i])
                    row.append(finall[nums - 1][i - 1] + finall[nums - 1][i])

                print(row)
            nums += 1
            finall.append(row)


        return finall
a=Solution.getRow([],5)
print(a)