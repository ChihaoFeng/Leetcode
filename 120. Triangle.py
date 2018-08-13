class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for level in range(1, n):
            row = triangle[level]
            for i, val in enumerate(row):
                if i == 0:
                    prev, dp[i] = dp[i], dp[i] + val
                elif i == level:
                    dp[i] = prev + val
                else:
                    prev, dp[i] = dp[i], min(dp[i], prev) + val
        return min(dp)

"""
Time: O(mn)
Space: O(n)
"""
