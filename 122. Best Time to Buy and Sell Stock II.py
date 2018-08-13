class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                ret += prices[i] - prices[i - 1]
        return ret


"""
Time: O(n)
Space: O(1)
"""