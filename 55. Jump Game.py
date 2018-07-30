class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        further = 0
        for i, num in enumerate(nums):
            if i > further:
                return False
            further = max(further, i + num)
        return True


"""
Like a gas station problem. further determines the farthest index we can go.
if we arrive an index that is beyond the farthest index, return False

Time: O(n)
Space: O(1)
"""
