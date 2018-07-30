class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        candidates = range(1, n + 1)
        stack = [1]
        for i in range(2, n):
            stack.append(stack[-1] * i)
        ret = ""
        k -= 1
        while stack and stack[-1] > k:
            stack.pop()
            ret += str(candidates.pop(0))
        while stack:
            val = stack.pop()
            ret += str(candidates.pop(k // val))
            k %= val
        return ret + ''.join(map(str, candidates))


"""
k         value (n = 4)
----------------
0          1234
1          1243
2          1324
3          1342
4          1423
5          1432
6          2134
7          2143
8          2314
9          2341
10         2413
11         2432
       .
       .
       .
       
candidates = [1, 2, 3, 4]
stack = [1, 2, 6]

eg. k = 9:
ret = ''
candidates = [1, 2, 3, 4]
9 / 6 = 1 ... 3  -> ret = '2', candidates = [1, 3, 4]
3 / 2 = 1 ... 1  -> ret = '23', candidates = [1, 4]
1 / 1 = 1 ... 0  -> ret = '234', candidates = [1]

ret += candidates


Time: O(n)
Space: O(n)
"""