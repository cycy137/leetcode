class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        tmp = "1"
        for i in range(2,n+1):
            mid_result=tmp
            mid_char=tmp[0]
            num=1
            if tmp=="1":
                tmp="11"

            for j in range(1,len(mid_result)):
                print(j,len(mid_result),mid_result)
                if tmp[j] == mid_char and j<len(mid_result)-1:
                    num += 1

                else :
                    tmp += str(num) + mid_char
                    mid_char = tmp[j]
                    # if j==len((mid_char)):
                    #     tmp = str(num) + str(tmp[j])




        return str(tmp)


a=Solution.countAndSay([],4)
print(a)