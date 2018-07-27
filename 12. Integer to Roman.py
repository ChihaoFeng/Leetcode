class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        ret = ''
        for v, s in zip(value, symbol):
            while num >= v:
                ret += s
                num -= v
            if num == 0:
                return ret
        raise ValueError


"""
The easiest way to solve this problem is to enumerate all six instances where subtraction is used with seven basic cases
Then we just iterate through the enumeration and generate the roman number

Time: O(n)
Space: O(n) 
"""
