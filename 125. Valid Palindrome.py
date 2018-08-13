class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s.lower())
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return True


"""
Time: O(n)
Space: O(n)
"""
