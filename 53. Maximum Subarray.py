class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ret = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            ret = max(ret, curr)
            if curr < 0:
                curr = 0
        return ret


"""
the idea is to keep adding until the sum is below 0. Then we set sum back to 0 and keep adding again

Time: O(n)
Space: O(1)
"""