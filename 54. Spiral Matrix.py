class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ptr = 0
        ret = []
        i = j = count = 0
        while count < m * n:
            ret.append(matrix[i][j])
            matrix[i][j] = None
            next_i = i + step[ptr][0]
            next_j = j + step[ptr][1]
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n or matrix[next_i][next_j] == None:
                ptr = (ptr + 1) % 4
                next_i = i + step[ptr][0]
                next_j = j + step[ptr][1]
            i, j = next_i, next_j
            count += 1
        return ret


"""
Time: O(m*n)
Space: O(1) if we are allowed to modify input matrix. otherwise, O(m*n)
"""
