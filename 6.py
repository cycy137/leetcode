class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        print(L)
        num, step = 0, 1

        for i in s:

            L[num] += i
            print(i,L)
            if num == 0:
                step = 1
            elif num == numRows -1:
                step = -1
            num += step

        return ''.join(L)

c=Solution.convert([],"PINALSIGYAHRPI",4)
print(c)