class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search_first():
            i, j, ret = 0, len(nums) - 1, -1
            while i <= j:
                m = (i + j) // 2
                if nums[m] == target:
                    ret = m
                    j = m - 1
                elif nums[m] > target:
                    j = m - 1
                else:
                    i = m + 1
            return ret

        def search_last():
            i, j, ret = 0, len(nums) - 1, -1
            while i <= j:
                m = (i + j) // 2
                if nums[m] == target:
                    ret = m
                    i = m + 1
                elif nums[m] > target:
                    j = m - 1
                else:
                    i = m + 1
            return ret

        if not nums:
            return [-1, -1]
        first = search_first()
        if first == -1:
            return [-1, -1]
        else:
            return [first, search_last()]


"""
Binary search implementation
Time: O(logn)
Space: O(1)
"""