class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        sign = x > 0
        x = abs(x)
        while x:
            ret = ret * 10 + x % 10
            x //= 10
        if not sign: ret *= -1
        return ret if - 2 ** 31 <= ret <= 2 ** 31 - 1 else 0

"""
The idea is pop the last digit from x using x%10 and push it to the end to ret
Be careful of the overflow

Time: O(log(n)) since there are around log10(n) digits for a number
Space: O(1)
"""