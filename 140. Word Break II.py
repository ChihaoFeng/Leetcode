class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def dfs(i):
            if i == len(s):
                return ['']
            if i in memo:
                return memo[i]
            temp = []
            for j in range(i + 1, len(s) + 1):
                string = s[i:j]
                if string in wordDict:
                    for sub in dfs(j):
                        temp.append(string + ' ' + sub if sub else string)
            memo[i] = temp
            return temp

        memo = {}
        wordDict = set(wordDict)
        return dfs(0)