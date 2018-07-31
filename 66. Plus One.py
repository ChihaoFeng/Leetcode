class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def backtrack(i=0):
            if i == len(digits) - 1:
                val = digits[i] + 1
                digits[i] = val % 10
                return val // 10
            val = digits[i] + backtrack(i + 1)
            digits[i] = val % 10
            return val // 10

        return [1] + digits if backtrack() else digits


"""
Time: O(n)
Space: O(1)
"""