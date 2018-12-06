class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<-8388608 or x >8388608:
            print("sdf")
            return 0
        tmp=str(abs(x))

        a=""
        for i in range(len(tmp)):
                a+=tmp[-1-i]
                print(a)
        if x!=abs(x) :
             a="-"+a
        return int(a)


c=Solution.reverse([],-2147483412)
print(c)

-2147483412
-8388608