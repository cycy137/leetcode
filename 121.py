class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minn=max(prices)
        maxx=0
        for i in range(len(prices)):

            if prices[i]<minn:
                minn=prices[i]
                #print(i)
            elif prices[i]-minn>maxx:
                #print(i)
                maxx=prices[i]-minn
        return maxx


a=Solution.maxProfit([],[7,1,5,3,6,4])
print(a)