class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(i, path, remain):
            if remain == 0:
                ret.append(path[:])
                return
            for j in range(i, len(candidates)):
                if j == i or candidates[j] != candidates[j - 1]:
                    if candidates[j] > remain:
                        return
                    path.append(candidates[j])
                    dfs(j + 1, path, remain - candidates[j])
                    path.pop()

        ret = []
        candidates.sort()
        dfs(0, [], target)
        return ret


"""
The difference between combinationSum2 and combinationSum1 is that each number
in candidates may only be used once. However, there will be duplicates in candidates.
Therefore, we need to avoid duplicates, which is similar to what we've done in 3sum.

Time: O(2^n)
Space: O(n)
"""
