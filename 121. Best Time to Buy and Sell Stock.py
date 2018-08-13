class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        ret = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > ret:
                ret = price - min_price
        return ret


"""
keep tracking the min price and updating the max profit

Time: O(n)
Space: O(1)
"""