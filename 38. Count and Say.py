class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            count, temp, _d = 0, '', s[0]
            for d in s:
                if d == _d:
                    count += 1
                else:
                    temp += str(count) + _d
                    _d = d
                    count = 1
            temp += str(count) + _d
            s = temp
        return s

"""
Time: O(n*k)
Space: O(n)
"""