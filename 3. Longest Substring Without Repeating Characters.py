class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        ret = 0
        i = 0
        for j, c in enumerate(s):
            if c in table:
                i = max(table[c] + 1, i)
            table[c] = j
            ret = max(ret, j - i + 1)
        return ret


"""
The idea is to use the lookup table to record last index of an element that we meet so far during iteration.
We use two pointers i, j pointing to the two ends of current substring we're dealing with. Whenever we meet 
an element that has been encountered before, we either set i to the index 
table[c] (last time this element appeared) + 1 or remain the same, and we choose the larger one to prevent redundant
traversal.

Time: O(n)
Space: O(n)
"""
print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring("aaa"))
print(Solution().lengthOfLongestSubstring("abcc"))
print(Solution().lengthOfLongestSubstring("abba"))
