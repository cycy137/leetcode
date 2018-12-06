class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len (s)
        dic ={}
        for i in range(n):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            elif t[i] in dic.values():
                return False;
            else:
                dic[s[i]] = t[i]
        return True
a = Solution.isIsomorphic([],"foo","bar")
print(a)

