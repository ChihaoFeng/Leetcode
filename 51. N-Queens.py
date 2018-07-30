class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def solve(pos):
            if pos == n:
                add_solution()
                return
            for i in range(n):
                queens[pos] = i
                if is_valid(pos):
                    solve(pos + 1)

        def is_valid(pos):
            for i in range(pos):
                if queens[i] == queens[pos]:
                    return False
                if abs(i - pos) == abs(queens[i] - queens[pos]):
                    return False
            return True

        def add_solution():
            board = []
            for i in queens:
                row = ['.'] * n
                row[i] = 'Q'
                board.append(''.join(row))
            ret.append(board)

        ret = []
        queens = [0] * n
        solve(0)
        return ret


"""
One key note is how to know whether two points are on the same diagonal line

index i, j for each elements:

(0,0)  (0,1)  (0,2)  (0,3)
(1,0)  (1,1)  (1,2)  (1,3)
(2,0)  (2,1)  (2,2)  (2,3)
(3,0)  (3,1)  (3,2)  (3,3)

we notice that (xi, xj) and (yi, yj) are on the same diagonal line if
|xi-yi| = |xj-yj|

Time: O(n*n)
Space: O(n)
"""