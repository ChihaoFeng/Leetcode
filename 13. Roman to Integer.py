class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        prev = float('inf')
        ret = 0
        for c in s:
            curr = table[c]
            if curr > prev:
                ret -= prev * 2
            ret += curr
            prev = curr
        return ret


"""
Generally speaking, the roman symbol is under descending order except some subtraction cases.
Here we use the prev variable to store the previous roman symbol's value. If the current symbol's
value is larger than the previous one, it means we encounter the subtraction cases. So we have
subtract prev once for the extra count and then add the curr value which is (curr - prev).

Time: O(n)
Space: O(n)
"""
