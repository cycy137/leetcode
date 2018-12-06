import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # tmp=""
        # if int(str)>(2**31-1):
        #     return 2**31-1
        # if int(str)<-2**31:
        #     return -2**31
        # for i in range(len(str)):
        #     if str[0]=="-":
        #
        #         str=str[1:]+" "
        #         tmp+="-"
        #
        #     if str[i].isdigit():
        #
        #         tmp+=str[i]
        #
        #     else:
        #         break
        # tmp=int(tmp)
        #
        # return tmp
        # print(str)

        ret = re.match(' *([-+]?\d+)',str)
        print(ret.groups())
        if ret:
            ret = int(ret.group(1))
            if ret>2**31-1:
                return 2**31-1
            if ret<-2**31:
                return -2**31
            return ret
        else:
            return 0

c = Solution.myAtoi([], "-4193 with sdf2342wo34234rds")
print(c)