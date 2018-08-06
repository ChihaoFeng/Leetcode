class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]


"""
# of node     number of unique BSTs
------------------------------------------------------------
    0                 1      
    1                 1
    2         dp[0] * dp[1] + dp[1] * dp[0]
    3         dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
         .
         .
         .
    n        dp[0] * dp[n-1] + dp[1] * dp[n-2] + ... + dp[n-1] * dp[0]


Time: O(n)
Space: O(n)

"""