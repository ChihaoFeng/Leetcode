class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        ret = 0
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ret = max(ret, i - stack[-1])
                else:
                    stack.append(i)
        return ret

    def longestValidParentheses_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ret = max(ret, left + right)
            elif left < right:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ret = max(ret, left + right)
            elif left > right:
                left = right = 0

        return ret


"""
sol1 uses a stack to record the index of '('. We put -1 at the beginning as a helper index.
whenever we encounter ')', we pop out the its corresponding '(' index, which should be on the top of 
stack. Then we can calculate the length based on the current peek value of stack.
However, if stack becomes empty after pop, it means that the current ')' is invalid. We need to again push
i as a helper index just like we push -1 at beginning. 

Time: O(n)
Space: O(n)

sol2 uses two counters to record number of '(' and ')' so far during iteration.
We are going to iterate s twice from left to right and right to left.

Time: O(n)
Space: O(1)

Though both solution have time complexity of O(n), sol1 will be faster since it only traverses s once.
"""
