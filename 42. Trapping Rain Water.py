class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        prev = water = 0
        for i in range(1, len(height)):
            if prev + height[i - 1] > height[i]:
                prev = prev + height[i - 1] - height[i]
                water += prev
            else:
                prev = 0
        prev = 0
        for i in range(len(height) - 2, -1, -1):
            if prev + height[i + 1] > height[i]:
                prev = prev + height[i + 1] - height[i]
                water += prev
            else:
                prev = 0

        return water + sum(height) - len(height) * max(height)

    def trap_1(self, height):
        left, right = 0, len(height) - 1
        min_height = 0
        ret = 0
        while left < right:
            while left < right and height[left] <= min_height:
                ret += min_height - height[left]
                left += 1
            while left < right and height[right] <= min_height:
                ret += min_height - height[right]
                right -= 1
            min_height = min(height[left], height[right])
        return ret


"""
For sol1, we're going to traverse height twice from left to right and right left.
When we traverse from left to right, we assume that the right end the infinity high
so that we only consider the limitation of left side. Same idea for right to left.
Finally, we can get the answer by applying water + sum(height) - area to get rid of the
redundant and repetition

For sol2, we only traverse the height once by having two pointers on two ends and moving inward.
We use a min_height as the limitation for both sides.

Time: O(n)
Space: O(1)
"""