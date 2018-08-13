class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curr = total = 0
        ret = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            curr += g - c
            if curr < 0:
                ret = i + 1
                curr = 0
        return ret if total >= 0 else -1