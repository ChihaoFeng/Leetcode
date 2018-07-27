class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(path='', left=0, right=0):
            if left + right == 2*n:
                ret.append(path)
                return
            if left < n:
                backtrack(path + '(', left + 1, right)
            if right < left:
                backtrack(path + ')', left, right + 1)

        ret = []
        backtrack()
        return ret

    def generateParenthesis_1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(path, i, count):
            if i == n:
                ret.append(path + ')'*count)
                return
            backtrack(path + '(', i + 1, count + 1)
            if count > 0:
                backtrack(path + ')', i, count - 1)

        ret = []
        backtrack('', 0, 0)
        return ret


"""
left and right count the number of '(' and ')' so far
'(' is limited by n
')' is limited by the number of '('
we can add ')' to the current path only if right < left

                    1   n
nth Catalan number --- C  
                   n+1  2n
                   
Time, Space: O(4^n/sqrt(n))
 
"""