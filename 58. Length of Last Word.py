class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ptr = len(s) - 1
        ret = 0
        while ptr >= 0 and s[ptr] == ' ':
            ptr -= 1
        while ptr >= 0 and s[ptr] != ' ':
            ret += 1
            ptr -= 1
        return ret