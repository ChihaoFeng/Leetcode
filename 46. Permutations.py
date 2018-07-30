class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(path):
            if len(path) == len(nums):
                ret.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] == '*':
                    continue
                path.append(nums[i])
                nums[i] = '*'
                dfs(path)
                nums[i] = path.pop()

        ret = []
        dfs([])
        return ret

