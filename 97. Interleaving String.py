class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1) + 1, len(s2) + 1
        T = [[False] * n for _ in range(m)]
        T[0][0] = True
        for i in range(1, m):
            if s1[i - 1] == s3[i - 1]:
                T[i][0] = T[i - 1][0]
        for j in range(1, n):
            if s2[j - 1] == s3[j - 1]:
                T[0][j] = T[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = (T[i - 1][j] if s1[i - 1] == s3[i + j - 1] else False) or (
                    T[i][j - 1] if s2[j - 1] == s3[i + j - 1] else False)
        return T[m - 1][n - 1]


"""
Time: O(m*n)
Space: O(m*n)
"""