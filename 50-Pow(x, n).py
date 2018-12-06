class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """


        def helper(x,n):
            if n==0:
                return 1.0
            y = helper(x,n//2)
            if n%2 == 0:
                return y*y
            else:return y*y*x
        if n >0 :
            return helper(x,n)
        else: return 1//helper(x,n)
a = Solution.myPow([],2.00000, 10)
print(a)