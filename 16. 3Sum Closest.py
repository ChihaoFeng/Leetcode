class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    temp = nums[i] + nums[j] + nums[k]
                    if temp == target:
                        return target
                    if abs(temp - target) < abs(ret - target):
                        ret = temp
                    if temp < target:
                        j += 1
                    else:
                        k -= 1
        return ret


"""
The idea is similar to three sum. We just need to have the ret hold the summation which is closest to target

Time: O(n^2)
Space: O(1)    
"""
