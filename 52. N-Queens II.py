def totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """

    def dfs(row):
        if row == n:
            self.ret += 1
            return
        for col in range(n):
            if cols[col] or d1[col - row + n - 1] or d2[row + col]:
                continue
            cols[col] = d1[col - row + n - 1] = d2[row + col] = True
            dfs(row + 1)
            cols[col] = d1[col - row + n - 1] = d2[row + col] = False

    self.ret = 0
    cols, d1, d2 = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
    dfs(0)
    return self.ret

"""
The idea is to have three lookup boolean array for columns and diagonals.

for diagonal k = 1, we use row + col as the index
for diagonal k = -1, we use col - row + n - 1 as the index

-----------------------------------------------------------------------------
eg. n = 4

index i, j for each elements:

(0,0)  (0,1)  (0,2)  (0,3)
(1,0)  (1,1)  (1,2)  (1,3)
(2,0)  (2,1)  (2,2)  (2,3)
(3,0)  (3,1)  (3,2)  (3,3)

-----------------------------------------------------------------------------
i + j for each elements:

0 1 2 3 |
-----------
0 1 2 3 | 
1 2 3 4 | 4
2 3 4 5 | 5
3 4 5 6 | 6

we can use that elements on the same diagonal line (k = 1) are same
index = i + j
-----------------------------------------------------------------------------
i - j for each elements:

  |       4   5   6
--------------------    
3 |   0   1   2   3
2 |  -1   0   1   2
1 |  -2  -1   0   1
0 |  -3  -2  -1   0

we can use that elements on the same diagonal line (k = -1) are same
index = i - j + n - 1


Time: O(n*n)
Space: O(n)
"""
