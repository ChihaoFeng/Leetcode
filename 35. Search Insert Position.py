class Solution:
    def searchInsert(self, nums, target):
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
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return i

    def searchInsert_handle_duplicate(self, nums, target):
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
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return i


"""
eg.

1    3    5    7                  target = 4
i    m         j
          i,m  j
          i,j,m
     j    i
     


1    3    5    5    5    7        target = 4
i         m              j
i,m  j
     i,j,m
     j    i



binary search
sol1 for no duplicates
sol2 handles duplicates

Time: O(logn)
Space: O(1)
"""