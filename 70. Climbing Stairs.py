class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        prev0, prev1 = 1, 2
        for _ in range(2, n):
            prev0, prev1 = prev1, prev0 + prev1
        return prev1


"""
typical dp problem
fibonacci number

Time: O(n)
Space: O(1)
"""