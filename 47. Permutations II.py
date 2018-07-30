class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(path):
            if len(path) == len(nums):
                ret.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] == '*' or (i > 0 and nums[i-1] == nums[i]):
                    continue
                path.append(nums[i])
                nums[i] = '*'
                dfs(path)
                nums[i] = path.pop()

        ret = []
        nums.sort()
        dfs([])
        return ret

