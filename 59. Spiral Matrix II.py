class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0] * n for _ in range(n)]
        count = 1
        ptr = i = j = 0
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while count <= n * n:
            ret[i][j] = count
            next_i, next_j = i + step[ptr][0], j + step[ptr][1]
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n or ret[next_i][next_j] != 0:
                ptr = (ptr + 1) % 4
                next_i, next_j = i + step[ptr][0], j + step[ptr][1]
            i, j = next_i, next_j
            count += 1
        return ret


"""
Time: O(m*n)
Space: O(m*n)
"""
