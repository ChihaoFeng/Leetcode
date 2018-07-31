class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i, j = 0, x
        while i <= j:
            m = (i + j) // 2
            if m * m == x:
                return m
            elif m * m < x:
                i = m + 1
            else:
                j = m - 1
        return j


"""
binary search problem

Time: O(logn)
Space: O(1)
"""
