class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(n):
            ret.extend([ret[j] | 1 << i for j in range(len(ret) - 1, -1, -1)])
        return ret

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        for i in range(1 << n):
            ret.append(i ^ (i >> 1))
        return ret


"""
Time: O(n)
Space: O(n)
"""