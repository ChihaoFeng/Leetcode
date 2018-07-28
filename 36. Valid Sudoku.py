class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols, squares = [0] * 9, [0] * 9, [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                value = 1 << int(board[i][j])
                if rows[i] & value or cols[j] & value or squares[3*(i//3)+(j//3)] & value:
                    return False
                rows[i] |= value
                cols[j] |= value
                squares[3 * (i // 3) + (j // 3)] |= value
        return True

"""
Use bit value to indicate whether the number exists in such row or col or square

Time: O(n^2)
Space: O(1)
"""