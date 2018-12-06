class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:return 0
        dp = len(s)*[0]
        for i in range(len(s)):
            if s[i] == ")":
                if i>0 and s[i-1] == "(":
                    dp[i] = dp[i-2]+2
                elif i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2]+2
                else:
                    dp[i] = 0


        print(dp)
        return max(dp)

a = Solution.longestValidParentheses([],"())((())")
print(a)