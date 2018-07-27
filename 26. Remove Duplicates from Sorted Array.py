class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

"""
The idea is to have a pointer j pointing to the boundary index where the left side of j should be non-duplicated string

Time: O(n)
Space: O(1)
"""