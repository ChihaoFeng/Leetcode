class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(t) + 1, len(s) + 1
        if m > n:
            return 0
        dp = [1] * n
        for i in range(1, m):
            prev = dp[i - 1]
            for j in range(i, n):
                if t[i - 1] == s[j - 1]:
                    prev, dp[j] = dp[j], prev + (dp[j - 1] if j != i else 0)
                else:
                    prev, dp[j] = dp[j], dp[j - 1] if j != i else 0
        return dp[n - 1]