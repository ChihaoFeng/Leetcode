class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [
            {'blank': 0, 'sign': 1, 'digit': 2, '.': 3},
            {'digit': 2, '.': 3},
            {'digit': 2, '.': 4, 'e': 5, 'blank': 8},
            {'digit': 4},
            {'digit': 4, 'e': 5, 'blank': 8},
            {'sign': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7, 'blank': 8},
            {'blank': 8}
        ]
        curr = 0
        for c in s:
            if c.isdigit():
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in 'E':
                c = 'e'
            elif c in {'+', '-'}:
                c = 'sign'
            if c not in state[curr].keys():
                return False
            curr = state[curr][c]
        return curr in {2, 4, 7, 8}


"""
The solution is based on DFA

Time: O(n) length of string
Space: O(1)
"""
