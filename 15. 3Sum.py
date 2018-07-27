class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ret = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[j] + nums[k] == -nums[i]:
                        ret.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        k -= 1
                    elif nums[j] + nums[k] < -nums[i]:
                        j += 1
                    else:
                        k -= 1
        return ret


"""
1. sort the array
2. set first pointer i from [0, n-2)
3. simplify to two sum problem where the array is from [i, n) and solve it using two pointers j, k

Time: O(n^2) = O(nlogn + n^2)
Space: O(1)
"""
