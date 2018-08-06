class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        x, y = len(matrix), len(matrix[0])
        i, j = 0, x * y - 1
        while i <= j:
            m = (i + j) // 2
            m_i = m // y
            m_j = m % y
            if matrix[m_i][m_j] == target:
                return True
            elif matrix[m_i][m_j] < target:
                i = m + 1
            else:
                j = m - 1
        return False


"""
think about it as binary search
Time: O(log(m*n))
Space: O(1)
"""