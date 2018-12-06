class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp=""
        i=0
        while i<len(str(x)):
            tmp+=str(x)[-1-i]
            print(tmp)
            i+=1
        # for i in range(len(x)):
        #     tmp+=x[-1+i]
        print (tmp)
        return (int(tmp)==x if True else False)

c = Solution.isPalindrome([], 1221)
print(c)