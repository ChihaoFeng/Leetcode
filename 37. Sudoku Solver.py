class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def pre_process():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        continue
                    val = 1 << int(board[i][j])
                    rows[i] |= val
                    cols[j] |= val
                    squares[3 * (i // 3) + j // 3] |= val

        def is_valid(i, j, c):
            val = 1 << int(c)
            if rows[i] & val or cols[j] & val or squares[3 * (i // 3) + j // 3] & val:
                return False
            return True

        def set_helper(i, j, c, flag):
            val = 1 << int(c)
            if flag:
                board[i][j] = c
                rows[i] |= val
                cols[j] |= val
                squares[3 * (i // 3) + j // 3] |= val
            else:
                board[i][j] = '.'
                rows[i] &= ~val
                cols[j] &= ~val
                squares[3 * (i // 3) + j // 3] &= ~val

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in '123456789':
                            if is_valid(i, j, c):
                                set_helper(i, j, c, True)
                                if solve():
                                    return True
                                set_helper(i, j, c, False)
                        return False
            return True

        rows, cols, squares = [0] * 9, [0] * 9, [0] * 9
        pre_process()
        solve()


"""
dfs, borrow the same idea from valid sudoku
Time: don't know
Space: don't know
"""