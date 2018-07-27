class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def removeElement_1(self, nums, val):
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return j + 1


"""
Sol1: use one pointer i pointing to the boundary index where the left side of i should be clear without target value
Sol2: use two pointer i, j where values on the right of j should all be target value

Time: O(n)
Space: O(1)
"""