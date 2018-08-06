class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1) + 1, len(word2) + 1
        ret = [[0] * n for _ in range(m)]
        for i in range(1, m):
            ret[i][0] = ret[i-1][0] + 1
        for j in range(1, n):
            ret[0][j] = ret[0][j-1] + 1
        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    ret[i][j] = ret[i-1][j-1]
                else:
                    ret[i][j] = min(ret[i-1][j-1], ret[i][j-1], ret[i-1][j]) + 1
        return ret[m-1][n-1]