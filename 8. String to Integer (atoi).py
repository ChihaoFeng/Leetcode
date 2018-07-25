import string


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        if not s:
            return 0

        sign = 1
        ret = 0
        i = 0
        if s[0] in {'+', '-'}:
            i = 1
            if s[0] == '-':
                sign = -1

        for j in range(i, len(s)):
            if s[j] in string.digits:
                ret = ret * 10 + int(s[j])
            else:
                break
        ret *= sign
        if sign == 1 and ret > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if sign == -1 and ret < -2 ** 31:
            return -2 ** 31
        return ret


"""
1. remove all whitespace from the beginning and end of str
2. check whether the first element of s is a sign so we can determine the sign of the int and also
   determine the starting index to traverse s
3. iterate through s and stop when we encounter the character which is not digit
4. check the overflow condition

Time: O(n) generally speaking it depends on the number of digits of the integer
Space: O(1)
"""

print(Solution().myAtoi('+1234'))
print(Solution().myAtoi('-1234'))
print(Solution().myAtoi('1234'))
print(Solution().myAtoi('  +12'))
print(Solution().myAtoi(' + 12'))
print(Solution().myAtoi('-91283472332'))