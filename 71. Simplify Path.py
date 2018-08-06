class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for file in path:
            if not file or file == '.':
                continue
            if file == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(file)
        return '/' + '/'.join(stack)