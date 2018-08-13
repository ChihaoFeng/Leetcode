class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ret = [[1]]
        for _ in range(1, numRows):
            ret.append([x + y for x, y in zip(ret[-1] + [0], [0] + ret[-1])])
        return ret