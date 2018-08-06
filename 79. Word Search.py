class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, pos):
            if pos == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[pos] != board[i][j]:
                return False
            board[i][j] = '*'
            for _i, _j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if dfs(_i, _j, pos + 1):
                    return True
            board[i][j] = word[pos]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
