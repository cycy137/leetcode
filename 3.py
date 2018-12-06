class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        finall=""

        tmp=0
        maxfinall=0
        for i in s:

            if i in finall:

                print(finall.split(i)[-1]+i)
                finall=finall.split(i)[-1]+i
                tmp=len(finall)
            else:
                tmp+=1
                finall+=i
                if tmp>=maxfinall:
                    maxfinall=tmp

            #print(finall)

        return maxfinall
c=Solution.lengthOfLongestSubstring([],"dvdf")
print(c)