class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def dfs(i):
            if i == len(s):
                return True
            if not memo[i]:
                return False
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and dfs(j):
                    return True
            memo[i] = False
            return False

        wordDict = set(wordDict)
        memo = [True] * len(s)
        return dfs(0)
