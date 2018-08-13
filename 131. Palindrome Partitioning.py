class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i, path):
            if i == len(s):
                ret.append(path[:])
                return
            for j in range(i + 1, len(s) + 1):
                if isPalindrome(s[i:j]):
                    path.append(s[i:j])
                    dfs(j, path)
                    path.pop()

        ret = []
        dfs(0, [])
        return ret