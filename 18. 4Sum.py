class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        ret = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i - 1] != nums[i]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j - 1] != nums[j]:
                        k, l = j + 1, len(nums) - 1
                        while k < l:
                            if nums[i] + nums[j] + nums[k] + nums[l] == target:
                                ret.append([nums[i], nums[j], nums[k], nums[l]])
                                while k < l and nums[k] == nums[k + 1]:
                                    k += 1
                                k += 1
                                while k < l and nums[l] == nums[l - 1]:
                                    l -= 1
                                l -= 1
                            elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                                k += 1
                            else:
                                l -= 1
        return


"""
Time: O(n^3)
Space: O(1)
"""
