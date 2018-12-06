class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        fin=0
        for i in range(len(s)):

            mid=ord(s[i])-64

            #print(i,mid)


            print(len(s),len(s)-i)
            mid*=26**(len(s)-1-i)
            print(mid)

            fin+=mid
        return fin

a=Solution.titleToNumber([],"AAA")
print(a)