class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while len(str(num))>1:
            n=0
            for i in list(str(num)):
                #print(i)
                n+=int(i)
                print(n)
            num=int(n)
            #print(num)
        return n


a=Solution.addDigits([],38)
print(a)