class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        i = 1
        for j in range(2, len(nums)):
            if nums[i] == nums[i-1] == nums[j]:
                continue
            i += 1
            nums[i] = nums[j]
        return i + 1


"""
i is the last index of subarray that satisfies the requirement

Time: O(n)
Space: O(1)
"""