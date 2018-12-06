class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=bin(num)
        b=str(a[2:])
        c=['0' if x == '1' else '1' for x in b]
        c="".join(c)

        # for i in b:
        #     print(i)
        #     if i =="0":
        #         i="1"
        #         print("yunxing",i)
        #     elif i =="1":
        #         i="0"

        return int(c,2)
a=Solution.findComplement([],5)
print(a)