class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        i = 0
        while i <= len(haystack) - len(needle):
            _i = i
            j = 0
            while haystack[_i] == needle[j]:
                _i += 1
                j += 1
                if j == len(needle):
                    return i
                if _i == len(haystack):
                    return -1
            i += 1
        return -1

"""
Naive Brute-Force solution
Time: O(m*n) where m, n are length of haystack and needle
Space: O(1)
"""