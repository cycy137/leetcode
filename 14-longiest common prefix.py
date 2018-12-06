class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # tmp=""
        # mid=0
        # if strs is None or len(strs) < 1 or len(strs[0]) < 1:
        #     return ""
        # while 1:
        #     if mid>=len(strs[0]):
        #         return tmp
        #     a=strs[0][mid]
        #     for i in range(1,len(strs)):
        #         print(mid,len(strs[i]),i)
        #         if mid>len(strs[i]) or strs[i][mid]!=a:
        #
        #             return tmp
        #         #print(a,strs[i][mid],mid)
        #     mid+=1
        #     tmp+=a
        if a!=None
        for a, b in enumerate(zip(*strs)):
            print(a,b)
            if len(set(b)) > 1:
                return strs[0][:a]
        else:
            return min(strs)
b=Solution.longestCommonPrefix([],["flower","flow","flight"])
print(b)