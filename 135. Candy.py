class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        n = len(ratings)
        dp = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i + 1] + 1)
        return sum(dp)
