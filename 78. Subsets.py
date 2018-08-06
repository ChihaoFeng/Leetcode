class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for num in nums:
            temp = [l + [num] for l in ret]
            ret.extend(temp)
        return ret

"""
Time: O(n)
Space: O(n)
"""