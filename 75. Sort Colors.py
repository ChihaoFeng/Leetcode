class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right, i = -1, len(nums), 0
        while i < right:
            if nums[i] == 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]
            elif nums[i] == 2:
                right -= 1
                nums[right], nums[i] = nums[i], nums[right]
                i -= 1
            i += 1

"""
we use left to record the right most index for 0s
we use right to record the left most index for 2s
left < i < right

Time: O(n)
Space: O(1)
"""