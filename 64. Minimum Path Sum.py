class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]


"""
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

The idea is to use dp to compute the minimum sum for each position.
The current sum only depends on the upper sum and left sum.
We need to calculate sums for first row and first column

Time: O(m*n)
Space: O(1)
"""