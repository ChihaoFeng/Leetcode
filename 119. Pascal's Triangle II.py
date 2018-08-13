class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [0] * (rowIndex + 1)
        ret[0] = 1
        for level in range(1, rowIndex + 1):
            for i in range(level, 0, -1):
                ret[i] += ret[i - 1]
        return ret
