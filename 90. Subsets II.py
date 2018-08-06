class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = [[]]
        prev = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                temp = [l + [num] for l in prev]
            else:
                temp = [l + [num] for l in ret]
            prev = temp
            ret.extend(temp)
        return ret

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(i, path):
            ret.append(path[:])
            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j + 1, path)
                path.pop()

        ret = []
        nums.sort()
        dfs(0, [])
        return ret


"""
Time: O(n)
Space: O(n)
"""