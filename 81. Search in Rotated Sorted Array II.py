class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            pivot = nums[m]
            if pivot == target:
                return True
            while i < m and nums[i] == nums[m]:
                i += 1
            while m < j and nums[j] == nums[m]:
                j -= 1
            if (pivot < nums[i]) != (target < nums[i]):
                if pivot < nums[i]:
                    pivot = float('inf')
                else:
                    pivot = float('-inf')
            if pivot < target:
                i = m + 1
            else:
                j = m - 1
        return False


"""
The only difference between the search in rotated sorted array I is we need to get rid of the duplicates

Time: O(n)
Space: O(1)
"""