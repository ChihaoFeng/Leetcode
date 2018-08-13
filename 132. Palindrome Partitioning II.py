class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        cut = [0] * n
        for i in range(n):
            min_cut = i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or pal[j+1][i-1]):
                    pal[j][i] = True
                    min_cut = 0 if j == 0 else min(min_cut, cut[j-1] + 1)
            cut[i] = min_cut
        return cut[-1]