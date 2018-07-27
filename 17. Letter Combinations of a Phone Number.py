class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def dfs(path, i):
            if i == len(digits):
                ret.append(path)
                return
            for c in table[digits[i]]:
                dfs(path + c, i + 1)

        if not digits:
            return []
        ret = []
        dfs('', 0)
        return ret


"""
simple dfs: traverse each possibility
Time: O(4^n)
Space: O(4^n + n) where O(4^n) the length of ret and O(n) is the table
"""
