class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1, p2 = 0, -1
        N = 2 * len(s) - 1
        for i in range(N):
            left = i // 2
            right = i // 2 + i % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > p2 - p1:
                    p1, p2 = left, right
                left -= 1
                right += 1
        return s[p1: p2+1]

"""
The idea is to expand around every possible center
eg. a b a b c
    |||||||||
Here we use i/2 and i/2 + i%2 as two pointers pointing to the head and tail of the possible palindrome

Time: O(n^2)
Space: O(1)
"""

