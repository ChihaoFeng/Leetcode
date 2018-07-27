class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p == '(':
                stack.append(')')
            elif p == '[':
                stack.append(']')
            elif p == '{':
                stack.append('}')
            elif not stack or stack.pop() != p:
                return False
        return len(stack) == 0


"""
The idea is to use the stack to record the complement of '(', '[', '{'

Time: O(n)
Space: O(n)
"""
