class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length = max(len(a), len(b))
        ret = ''
        c = 0
        for i in range(length):
            x = int(a[len(a) - 1 - i]) if i < len(a) else 0
            y = int(b[len(b) - 1 - i]) if i < len(b) else 0
            s = c + x + y
            ret = str(s % 2) + ret
            c = s // 2
        return '1' + ret if c else ret


"""
Just reversely go through two strings and and add up. If the index is out of range, add it as 0

Time: O(max(m, n))
Space: O(max(m, n))
"""
