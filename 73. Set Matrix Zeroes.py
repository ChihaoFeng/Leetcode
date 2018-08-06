class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0


"""
The idea is to use use first row and column as a look up entry
if matrix[i][j] = 0 if matrix[i][0] == 0 or matrix[0][j] == 0
we will have an extra col0 to determine the condition of first column

Time: O(m*n)
Space: O(1)
"""