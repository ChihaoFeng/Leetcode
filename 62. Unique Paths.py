class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n < 2:
            return 1
        dp = [1] * m
        for _ in range(2, n):
            for i in range(1, m):
                dp[i] += dp[i - 1]
        return sum(dp)

    def uniquePaths_1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def combination(n, k):
            ret = 1
            while k > 0:
                ret *= (n / k)
                n -= 1
                k -= 1
            return ret

        if n < 1:
            return 0
        if n < 2:
            return 1
        n -= 1
        m -= 1
        if n > m:
            m, n = n, m
        return int(round(combination(m + n, n)))

    def uniquePaths_2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = [0] * n
        ret[0] = 1
        for i in range(m):
            for j in range(1, n):
                ret[j] += ret[j-1]
        return ret[-1]


"""
sol1:
suppose m = 5

n = 1:
x x x x x
-------------------
n = 2:
 x  x  x  x  x
 x  x  x  x  x

 1  1  1  1  1  = dp
-------------------
n = 2:
 x  x  x  x  x
 x  x  x  x  x
 x  x  x  x  x

 5  4  3  2  1  = dp
-------------------
n = 2:
 x  x  x  x  x
 x  x  x  x  x
 x  x  x  x  x
 x  x  x  x  x

15 10  6  3  1  = dp

Time: O(m*n)
Space: O(m)



sol2:
suppose m = 5, n = 3
We have 5 Rs and 3 Ds in total.
Therefore, we have 8 slots and need to select 3 slots for D and the other for R
result would be ( 8 )   (m+n)!
                ( 3 )  --------
                         m!n!

Time: O(n) n < m
Space: O(1)

sol3:

  [1,0,0]
  [0,0,0]
  [0,0,0]
  
  [1,1,1]
  [1,2,3]   => ret[i] = ret[k] (i-1, j) + ret[k-1] (i, j-1) for i in range(1,m) for j in range(0,n) 
  [1,3,6]

Time: O(m*n)
Spcae: O(n)
"""
