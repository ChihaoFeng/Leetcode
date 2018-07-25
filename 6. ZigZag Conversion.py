class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        ret = [''] * numRows
        row = 0
        step = 1
        for c in s:
            ret[row] += c
            if row + step < 0 or row + step == numRows:
                step *= -1
            row += step
        return ''.join(ret)


"""
The idea is to have an array that stores result from each row. 
We use "step" here to define the current direction.

Time: O(n)
Space: O(n)
"""

