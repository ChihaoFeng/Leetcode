class Solution:
    def combinationSum(self, candidates, target):
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
                if candidates[j] > remain:
                    break
                path.append(candidates[j])
                dfs(j, path, remain - candidates[j])
                path.pop()

        ret = []
        candidates.sort()
        dfs(0, [], target)
        return ret


"""
Time: O(2^n) similar to the number of subsets for n elements
Space: O(n)
"""