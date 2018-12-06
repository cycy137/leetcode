class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        finall = ""
        while n > 26:
            mod = n % 26
            if not mod:
                print("hjkh",n)
                mod = 26
                n -= 1

            finall = chr(64 + mod) + finall
            print(finall)

            n //= 26
            print(n)
        if n > 0:
            finall = chr(64 + n) + finall
        return finall

        # a = []
        # finall = ""
        #
        # while n > 26:
        #     a.insert(0, n % 26)
        #     n = n // 26
        #
        # a.insert (0,n)
        # print(a)
        # for i in range(len(a)):
        #     print(a, finall)
        #
        #     if a[-1]==0:
        #         a[0]=a[0]-1
        #         a[-1]=26
        #     print(a)
        #     finall += chr(a[i] + 64)
        #     #print(a, finall)
        # return finall


c=Solution.convertToTitle([],701)
print(c)