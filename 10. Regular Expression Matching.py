class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        T = [[False] * (n + 1) for _ in range(m + 1)]
        T[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                T[0][j] = T[0][j - 1] or T[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    T[i][j] = T[i - 1][j - 1]
                elif p[j - 1] == '*':
                    T[i][j] = T[i][j - 2] or (T[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)
        return T[m][n]


"""
dp solution: use a 2d table to record result of match between s[:i] and p[:j]
1. if s[i-1] == p[j-1] or p[j-1] is '.':
        T[i][j] = T[i-1][j-1]
2. if p[j-1] is '*':
        a. check what happen if zero of the preceding element: T[i][j-2] (* for zero of the preceding element)
        b. if p[j-2] == s[i-1] or p[j-2] is '.':
                check whether s[i-2] matches p[j-1]: T[i-1][j] 
                (* for more of the preceding element, eg. a vs c*a*, aa vs c*a*)

Time: O(m*n)
Space: O(m*n)
"""

print(Solution().isMatch('aab', 'c*a*b'))
