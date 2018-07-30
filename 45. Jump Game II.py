class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_end = curr_farthest = ret = 0
        for i in range(len(nums) - 1):
            curr_farthest = max(curr_farthest, i + nums[i])
            if i == curr_end:
                curr_end = curr_farthest
                ret += 1
        return ret

    def jump_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        start = end = level = 0
        while start <= end:
            for curr in range(start, end + 1):
                if curr + nums[curr] >= len(nums) - 1:
                    return level + 1
                end = max(end, curr + nums[curr])
            start = curr + 1
            level += 1
        return -1

"""
sol1 is based on greedy.
sol2 is based on bfs.

Time: O(n)
Space: O(1)
"""