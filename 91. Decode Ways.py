class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        prev0, prev1 = 1, 1
        for i in range(1, len(s)):
            prev0, prev1 = prev1, (prev1 if s[i] != '0' else 0) + (prev0 if 10 <= int(s[i - 1:i + 1]) <= 26 else 0)
        return prev1


"""
(prev1 if s[i] != '0' else 0) + (prev0 if 10 <= int(s[i - 1:i + 1]) <= 26 else 0)

Time: O(n)
Space: O(1)
"""