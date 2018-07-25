class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], i]
            table[num] = i
        return []


"""
The basic idea is to have a lookup table to record the element and its index (val: index) in nums.
Before we store the element, we first need to check whether the element's complement has already in
the table. If it exists, it turns out we have found a solution which is the current index (i) and the 
complement's index (table[target - num]).

Time: O(n)
Space: O(n)
"""
print(Solution().twoSum([2, 7, 11, 15], 9))
