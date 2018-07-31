class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ret = [0] * n
        ret[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    ret[j] = 0
                elif j > 0:
                    ret[j] += ret[j-1]
        return ret[-1]


"""
The idea is just same as Unique Paths.
we just need to set ret[j] = 0 if we meet the obstacle

Time: O(m*n)
Space: O(n)
"""