class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = 0
        for num in nums:
            first = (first ^ num) & (~second)
            second = (second ^ num) & (~first)
        return first
