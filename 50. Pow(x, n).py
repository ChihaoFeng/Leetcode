class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def myPow_helper(x, n):
            if n == 1:
                return x
            val = myPow_helper(x, n // 2)
            if n % 2:
                return val * val * x
            else:
                return val * val

        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x, n = 1/x, -n
        return myPow_helper(x, n)

"""
The idea is to calculate the result of x^(n/2) and then return result*result
Time: O(logn)
Space: O(1) 
"""