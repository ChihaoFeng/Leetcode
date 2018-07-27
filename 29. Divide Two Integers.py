class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ret = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while temp <= dividend:
                dividend -= temp
                ret += i
                i <<= 1
                temp <<= 1
        if not positive:
            ret *= -1
        if ret < -2**31 or ret > 2**31 - 1:
            return 2**31 - 1
        return ret


"""
In order to increase speed to get the result we can do:
Y = 1*x + 2*x + 4*x + ... k*x + 1*x + 2*x + ... + z
if k*x > Y, k goes back to 1

Explanation for time complexity from user x11317x:
Consider this case: dividend = 2^31 - 1 = 2147483647, divisor = 2, the process is
2147483647 = 2 * 2^29 + 1073741823 (dividend = divisor * quotient + remainder)
1073741823 = 2 * 2^28 + 536870911
...
So the time complexity is 29 + 28 + ... + 1 = (29 + 1) * 29 / 2 = 435 = O(1)


Time: O(1)
Space: O(1)
"""
