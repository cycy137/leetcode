class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0;
        start = -1
        flag = []
        for i in range(len(s)):

           if s[i] == "(":
               flag.append(i)
           else:
               if len(flag) == 0:
                   start = i
               else:
                   tmp = flag[-1]
                   flag.pop()
                   if len(flag) == 0:
                        res =max(res,i-start)
                   else:
                       res = max(res, i - flag[0])

        return res
a= Solution.longestValidParentheses([],"(()()")
print(a)