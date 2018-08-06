class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(i, remain, path):
            if not remain:
                ret.append(path[:])
                return
            for j in range(i, n + 1 - (remain - 1)):
                path.append(j)
                dfs(j + 1, remain - 1, path)
                path.pop()

        ret = []
        dfs(1, k, [])
        return ret
