class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not s or not p: return False
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # initialize the first row.
        for j in range(1, m+1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

                # First column is already all False

        for i in range(1, n+1):
            #print(m)
            for j in range(1, m+1):
                #print("dsds")
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    print(i,j,dp)
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        #print(dp)
        return dp[-1][-1]
a = Solution.isMatch([],"aa","*")
print(a)