import collections


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        S = "ADOBECODEBANC", T = "ABC"
        """
        needs = collections.Counter(t)
        missing = len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            if needs[c] > 0:
                missing -= 1
            needs[c] -= 1
            if not missing:
                while i < j and needs[s[i]] < 0:
                    needs[s[i]] += 1
                    i += 1
                if J == 0 or j - i < J - I:
                    I, J = i, j
        return s[I:J]


"""
needs counts the number of characters in t
missing records the number of characters we are missing in current substring
I, J determine the current minimum substring we have 

traverse through s, if the character is what we need (c in needs), missing -= 1.
We also decrease the needs[c] even if c is not in T. Negative value means we have
redundant characters in our substring. Then we need shorten the current substring by
popping out the index with negative needs

Time: O(n)
Space: O(n)
"""