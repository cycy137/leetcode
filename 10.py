import re
class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ret = re.search(p, s)

        #ret = re.match(' *([-+]?\d+)',s)
        print(ret.group())
        return True if ret.group()==s else False

#c = Solution.isMatch([], "mississippi","mis*is*ip*i")
c = Solution.isMatch([], "aa","a")
print(c)