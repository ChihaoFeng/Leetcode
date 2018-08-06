class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret = 0
        stack = [-1]
        for i, height in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= height:
                ret = max(ret, heights[stack.pop()] * (i - 1 - stack[-1]))
            stack.append(i)
        while stack[-1] != -1:
            ret = max(ret, heights[stack.pop()] * (len(heights) - 1 - stack[-1]))
        return ret


"""
The idea is to keep push the current index to stack until the current height is less or equal to previous height.
In that case, we can update the maximum rectangle area comparing to the current area = heights[stack.pop()] * (i - 1 - stack[-1])

Time: O(n)
Space: O(n)
"""