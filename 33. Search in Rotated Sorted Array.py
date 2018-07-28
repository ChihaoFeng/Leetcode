class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            pivot = nums[m]
            if (nums[m] < nums[0]) != (target < nums[0]):
                if nums[m] < nums[0]:
                    pivot = float('inf')
                else:
                    pivot = float('-inf')
            if pivot < target:
                i = m + 1
            elif pivot > target:
                j = m
            else:
                return m
        return -1


"""
The idea is to use binary search to find the number.
However, we should first determine whether nums[m] is on the same side with target.
If not, we should push m to the correct partition in next iteration.

Time: O(logn)
Space: O(1) 
"""