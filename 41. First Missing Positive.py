class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1


"""
the idea is to move the the element to the correct position where nums[i] == nums[nums[i] - 1]
the expected array be [1, ..., n]. We keep swapping the element to the correct position except
the element's value is out of our expected scope.

Time: O(n)
Space: O(1)
"""
