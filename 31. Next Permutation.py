class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                j = len(nums) - 1
                while nums[j] <= nums[i - 1]:
                    j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break
            i -= 1
        reverse(i, len(nums) - 1)


"""
1. Find i where nums[i] > nums[i-1]
2. Find the smallest nums[j] > nums[i-1] in range [i, len(nums))
3. Swap i-1 and j
4. Reverse the array from i to the end

1   5   8   4   7   6   5   3   1
           i-1  i
                        j
1   5   8   5   7   6   4   3   1
1   4   8   5   1   3   4   6   7

Time: O(n)
Space: O(1)
"""
