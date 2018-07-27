class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ret = 0
        i, j = 0, len(height) - 1
        while i < j:
            ret = max(ret, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ret


"""
We first take two pointers pointing to the beginning and end of the array so that we have the largest width
for the rectangle. Then we are going to move one of the pointer inward to attempt to get larger rectangle.
in order to increase the area, we should move the shorter line. Otherwise, the area is limited by the shorter
line so we won't get larger area.

Time: O(n)
Space: O(1)
"""
