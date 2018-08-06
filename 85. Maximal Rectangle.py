class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * (len(matrix[0]) + 1)
        ret = 0
        for row in matrix:
            for i, num in enumerate(row):
                heights[i] = heights[i] + 1 if num == '1' else 0
            stack = [-1]
            for j, height in enumerate(heights):
                while stack[-1] != -1 and heights[stack[-1]] >= height:
                    ret = max(ret, heights[stack.pop()] * (j - 1 - stack[-1]))
                stack.append(j)
        return ret


"""
We can use the same idea as computing the largest rectangle in histogram where we update the histogram by traversing
each row of matrix

Time: O(m*n)
Space: O(n)
"""